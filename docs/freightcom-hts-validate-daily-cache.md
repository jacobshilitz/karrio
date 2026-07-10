# freightcom_rest: daily HTS validate + cache

Tracking design for CA→US `hsverified` / Zonos HTS validation in the
**`jacobshilitz/karrio-community`** plugin (`community/plugins/freightcom_rest`).

> Note: GitHub Issues are disabled on both `jacobshilitz/karrio` and
> `jacobshilitz/karrio-community`. This draft PR tracks the work.

## Context

Freightcom API 2.8.0 requires `POST /shipment/hts-validate` before `hsverified: true`.
Ticket **8664383**: do not cache validate results > **1 day**; re-validate daily.

Client hardcoding (`freightcom_hts_validated` + static HS description) fails because
`recommended_array` descriptions drift (observed May 11 / May 25 / Jul 9 for `4911.99.8000`).

Related: GitLab `zencart/chequesplus#1023`.

## Plan (implement in karrio-community plugin)

1. `proxy.validate_hts()` → `POST /shipment/hts-validate`
2. `utils.resolve_hts()` with `connection_cache`, TTL **86400**
3. `rate.py` + `shipment/create.py`: map recommended → `hs_code`/`description`,
   originals → `provided_*`, set `hsverified` when guaranteed customs requested
4. Deprecate client `freightcom_hts_validated` as source of truth

## Acceptance

- [ ] First CA→US rate of the day calls validate; same product later hits 24h cache
- [ ] Correct recommended vs provided field mapping
- [ ] Unit tests with mocked validate + cache hit
- [ ] No Chequesplus/Honeydew change required after ShipNGo deploys plugin

## Status

Open — not implemented yet.
