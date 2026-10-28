import karrio.schemas.fedex.tracking_document_request as fedex
import datetime
import gzip
import hashlib
import typing
import urllib.parse
import karrio.lib as lib
import karrio.core as core


class Settings(core.Settings):
    """FedEx connection settings."""

    api_key: str = None
    secret_key: str = None
    account_number: str = None
    track_api_key: str = None
    track_secret_key: str = None

    account_country_code: str = None
    metadata: dict = {}
    config: dict = {}
    id: str = None

    @property
    def carrier_name(self):
        return "fedex"

    @property
    def server_url(self):
        return (
            "https://apis-sandbox.fedex.com"
            if self.test_mode
            else "https://apis.fedex.com"
        )

    @property
    def tracking_url(self):
        return "https://www.fedex.com/fedextrack/?trknbr={}"

    @property
    def default_currency(self) -> typing.Optional[str]:
        return lib.units.CountryCurrency.map(self.account_country_code).value

    @property
    def connection_config(self) -> lib.units.Options:
        from karrio.providers.fedex.units import ConnectionConfig

        return lib.to_connection_config(
            self.config or {},
            option_type=ConnectionConfig,
        )


def get_proof_of_delivery(tracking_number: str, settings: Settings):
    import karrio.providers.fedex.error as error

    request = fedex.TrackingDocumentRequestType(
        trackDocumentSpecification=[
            fedex.TrackDocumentSpecificationType(
                trackingNumberInfo=fedex.TrackingNumberInfoType(
                    trackingNumber=tracking_number
                )
            )
        ],
        trackDocumentDetail=fedex.TrackDocumentDetailType(
            documentType="SIGNATURE_PROOF_OF_DELIVERY",
            documentFormat="PNG",
        ),
    )
    response = lib.to_dict(
        lib.request(
            url=f"{settings.server_url}/track/v1/trackingdocuments",
            trace=settings.trace_as("json"),
            data=lib.to_json(request),
            method="POST",
            decoder=parse_response,
            on_error=lambda b: parse_response(b.read()),
        )
    )

    messages = error.parse_error_response(response, settings)

    if any(messages):
        return None

    return lib.failsafe(
        lambda: lib.bundle_base64(response["output"]["documents"], format="PNG")
    )


def parse_response(binary_string):
    content = lib.failsafe(lambda: gzip.decompress(binary_string)) or binary_string
    return lib.decode(content)


def state_code(address: lib.units.ComputedAddress) -> str:
    if address.state_code is None:
        return None

    return (
        "PQ"
        if address.state_code.lower() == "qc" and address.country_code == "CA"
        else address.state_code
    )


def _format_postal(postal_code: typing.Optional[str], country_code: typing.Optional[str]) -> typing.Optional[str]:
    if not postal_code:
        return postal_code
    compact = postal_code.replace(" ", "").upper()
    if country_code == "CA" and len(compact) == 6:
        return f"{compact[:3]} {compact[3:]}"
    return postal_code


def _address_fingerprint(address: lib.units.ComputedAddress) -> str:
    street = "|".join(address.address_lines or [])
    raw = "|".join(
        [
            street,
            address.city or "",
            address.state_code or "",
            (address.postal_code or "").replace(" ", "").upper(),
            address.country_code or "",
        ]
    ).upper()
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _shipping_access_token(settings: Settings) -> str:
    cache_key = f"{settings.carrier_name}|{settings.api_key}|{settings.secret_key}"

    def get_token():
        response = lib.request(
            url=f"{settings.server_url}/oauth/token",
            method="POST",
            headers={"content-Type": "application/x-www-form-urlencoded"},
            data=urllib.parse.urlencode(
                dict(
                    grant_type="client_credentials",
                    client_id=settings.api_key,
                    client_secret=settings.secret_key,
                )
            ),
            decoder=lib.to_dict,
        )
        expiry = datetime.datetime.now() + datetime.timedelta(
            seconds=float(response.get("expires_in", 0))
        )
        return {**response, "expiry": lib.fdatetime(expiry)}

    return settings.connection_cache.thread_safe(
        refresh_func=get_token,
        cache_key=cache_key,
        buffer_minutes=30,
    ).get_state()


def _resolve_batch(
    addresses: typing.List[lib.units.ComputedAddress],
    settings: Settings,
) -> typing.Dict[str, str]:
    """Call FedEx Address Validation; return fingerprint → resolved city."""
    if not addresses:
        return {}

    token = _shipping_access_token(settings)
    payload = {
        "addressesToValidate": [
            {
                "clientReferenceId": _address_fingerprint(address),
                "address": {
                    "streetLines": [
                        lib.text(line, max=35)
                        for line in (address.address_lines or ["1 MAIN ST"])[:3]
                        if line
                    ]
                    or ["1 MAIN ST"],
                    "city": address.city,
                    "stateOrProvinceCode": state_code(address),
                    "postalCode": _format_postal(
                        address.postal_code, address.country_code
                    ),
                    "countryCode": address.country_code,
                },
            }
            for address in addresses
        ]
    }
    raw = lib.request(
        url=f"{settings.server_url}/address/v1/addresses/resolve",
        method="POST",
        data=lib.to_json(payload),
        headers={
            "content-type": "application/json",
            "authorization": f"Bearer {token}",
            "x-locale": "en_US",
        },
        decoder=parse_response,
        on_error=lambda b: parse_response(b.read()),
        trace=settings.trace_as("json"),
    )
    response = lib.to_dict(raw) if not isinstance(raw, dict) else raw
    if not isinstance(response, dict):
        return {}

    resolved: typing.Dict[str, str] = {}
    for entry in (response.get("output") or {}).get("resolvedAddresses") or []:
        # FedEx returns clientReferenceId on the entry or nested resolvedAddress
        ref = entry.get("clientReferenceId") or (
            (entry.get("resolvedAddress") or {}).get("clientReferenceId")
        )
        ra = entry.get("resolvedAddress") or entry
        city = ra.get("city")
        if ref and city:
            resolved[ref] = city

    # Some responses use a flat list keyed only by order — fall back by index
    if not resolved:
        entries = (response.get("output") or {}).get("resolvedAddresses") or []
        for address, entry in zip(addresses, entries):
            ra = entry.get("resolvedAddress") or entry
            city = ra.get("city")
            if city:
                resolved[_address_fingerprint(address)] = city

    return resolved


def resolve_address_cities(
    addresses: typing.Sequence[typing.Optional[lib.units.ComputedAddress]],
    settings: Settings,
) -> typing.Dict[int, str]:
    """Map id(address) → city using FedEx Address Validation (cached).

    Soft-fails: any AV/auth error keeps the original city. Only addresses with
    a city or postal are resolved; others pass through unchanged.
    """
    usable = [
        address
        for address in addresses
        if address is not None and (address.city or address.postal_code)
    ]
    by_id: typing.Dict[int, str] = {
        id(address): address.city for address in usable
    }
    if not usable:
        return by_id

    cache = settings.connection_cache
    pending_by_fp: typing.Dict[str, lib.units.ComputedAddress] = {}

    for address in usable:
        fp = _address_fingerprint(address)
        cached = cache.get(f"fedex|av|{fp}")
        if isinstance(cached, dict) and cached.get("city"):
            by_id[id(address)] = cached["city"]
        elif fp not in pending_by_fp:
            pending_by_fp[fp] = address

    if pending_by_fp:
        pending = list(pending_by_fp.values())
        resolved = lib.failsafe(lambda: _resolve_batch(pending, settings)) or {}
        for fp, address in pending_by_fp.items():
            city = resolved.get(fp) or address.city
            if fp in resolved:
                cache.set(f"fedex|av|{fp}", {"city": city}, timeout=7 * 24 * 3600)

        for address in usable:
            fp = _address_fingerprint(address)
            if fp in resolved:
                by_id[id(address)] = resolved[fp]
            else:
                cached = cache.get(f"fedex|av|{fp}")
                if isinstance(cached, dict) and cached.get("city"):
                    by_id[id(address)] = cached["city"]

    return by_id


def apply_preferred_cities(
    labeled: typing.Dict[str, typing.Optional[lib.units.ComputedAddress]],
    cities: typing.Dict[int, str],
    preferred: typing.Optional[dict],
) -> typing.Dict[int, str]:
    """Overlay rate-meta resolved cities onto the AV city map (rate → ship handoff)."""
    if not preferred:
        return cities

    out = dict(cities)
    for key, address in labeled.items():
        if address is None:
            continue
        patch = preferred.get(key) or {}
        city = patch.get("city")
        if city:
            out[id(address)] = city
    return out


def resolved_addresses_meta(
    labeled: typing.Dict[str, typing.Optional[lib.units.ComputedAddress]],
    cities: typing.Dict[int, str],
) -> dict:
    """Build rate/shipment meta.resolved_addresses for handoff + UI."""
    meta: dict = {}
    for key, address in labeled.items():
        if address is None or not (address.city or address.postal_code):
            continue
        city = cities.get(id(address), address.city)
        original = address.city
        meta[key] = dict(
            city=city,
            city_original=original,
            changed=bool(
                city
                and original
                and city.strip().upper() != original.strip().upper()
            ),
            state_code=address.state_code,
            postal_code=address.postal_code,
            country_code=address.country_code,
        )
    return meta


def resolved_city(
    address: typing.Optional[lib.units.ComputedAddress],
    settings: Settings,
    cities: typing.Optional[typing.Dict[int, str]] = None,
) -> typing.Optional[str]:
    """City for a FedEx address payload — AV / preferred result when available."""
    if address is None:
        return None
    if cities is not None and id(address) in cities:
        return cities[id(address)]
    return resolve_address_cities([address], settings).get(id(address), address.city)
