import karrio.schemas.fedex.tracking_document_request as fedex
import gzip
import typing
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


# Former Toronto municipalities FedEx often rejects for M* postals.
_TORONTO_BOROUGHS = {
    "NORTH YORK",
    "SCARBOROUGH",
    "ETOBICOKE",
    "EAST YORK",
    "YORK",
    "WILLOWDALE",
    "DON MILLS",
    "WESTON",
    "REXALE",
    "REXDALE",
    "DOWNSVIEW",
    "EAST YORK",
}

# Official / postal-city names FedEx accepts (from prod POSTALCITY.MISMATCH).
_CITY_ALIASES = {
    "GREATER SUDBURY": "Sudbury",
    "POINT CLAIRE": "Pointe-Claire",
    "POINTE CLAIRE": "Pointe-Claire",
    "WHITCHURCH-STOUFFVILLE": "Stouffville",
    "WHITCHURCH STOUFFVILLE": "Stouffville",
    "ASPHODAL-NORWOOD": "Norwood",
    "ASPHODAL NORWOOD": "Norwood",
    "ASPHODEL-NORWOOD": "Norwood",
    "ASPHODEL NORWOOD": "Norwood",
    "NEW TECUMSETH": "Alliston",
    "QUINTE WEST": "Trenton",
    "CORMAN PARK": "Saskatoon",
    "NORTH SAANICH": "Sidney",
    "GUELPH/ERAMOSA": "Guelph",
    "GUELPH ERAMOSA": "Guelph",
    "CENTRE WELLINGTON": "Fergus",
    "GEORGINA": "Keswick",
    "LES CEDRES": "Les Cedres",
    "COTE SAINT-LUC": "Cote Saint-Luc",
    "COTE-SAINT-LUC": "Cote Saint-Luc",
    "KAWARTHA LAKES": "Lindsay",
    "CHATHAM-KENT": "Chatham",
    "CHATHAM KENT": "Chatham",
}

# When the municipality name is wrong for the FSA (prod offenders).
_FSA_CITY_OVERRIDE = {
    "L5J": "Mississauga",  # often labeled Oakville
    "M6S": "Toronto",  # often labeled Mississauga
}


def normalize_city(
    city: typing.Optional[str],
    postal_code: typing.Optional[str] = None,
    country_code: typing.Optional[str] = None,
) -> typing.Optional[str]:
    """Map common CA city labels to FedEx-accepted postal cities.

    Reduces DESTINATION.POSTALCITY.MISMATCH noise from amalgamated
    municipalities, Toronto boroughs, and known misspellings.
    """
    if not city:
        return city

    fsa = (postal_code or "").replace(" ", "").upper()[:3]
    key = " ".join(city.strip().upper().replace("/", " ").split())

    if country_code == "CA" and fsa in _FSA_CITY_OVERRIDE:
        return _FSA_CITY_OVERRIDE[fsa]

    if country_code == "CA" and fsa.startswith("M") and key in _TORONTO_BOROUGHS:
        return "Toronto"

    if key in _CITY_ALIASES:
        return _CITY_ALIASES[key]

    if key.startswith("GREATER ") and len(key) > 8:
        return city.strip()[8:].strip() or city

    return city
