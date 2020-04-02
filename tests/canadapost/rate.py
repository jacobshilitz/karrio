import unittest
from unittest.mock import patch
from purplship.core.utils.helpers import to_dict
from purplship.package import rating
from purplship.core.models import RateRequest
from tests.canadapost.fixture import gateway
from datetime import datetime


class TestCanadaPostRating(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.RateRequest = RateRequest(**RatePayload)

    def test_create_rate_request(self):
        request = gateway.mapper.create_rate_request(self.RateRequest)

        self.assertEqual(request.serialize(), RateRequestXML)

    def test_create_rate_request_with_package_preset(self):
        request = gateway.mapper.create_rate_request(
            RateRequest(**RateWithPresetPayload)
        )

        self.assertEqual(request.serialize(), RateRequestUsingPackagePresetXML)

    @patch("purplship.package.mappers.canadapost.proxy.http", return_value="<a></a>")
    def test_create_rate_request_with_package_preset_missing_weight(self, _):
        processing_error = (
            rating.fetch(RateRequest(**RateWithPresetMissingWeightPayload))
            .from_(gateway)
            .parse()
        )

        self.assertEqual(to_dict(processing_error), to_dict(ProcessingError))

    @patch("purplship.package.mappers.canadapost.proxy.http", return_value="<a></a>")
    def test_get_rates(self, http_mock):
        rating.fetch(self.RateRequest).from_(gateway)

        url = http_mock.call_args[1]["url"]
        self.assertEqual(url, f"{gateway.proxy.settings.server_url}/rs/ship/price")

    def test_parse_rate_response(self):
        with patch("purplship.package.mappers.canadapost.proxy.http") as mock:
            mock.return_value = RateResponseXml
            parsed_response = rating.fetch(self.RateRequest).from_(gateway).parse()

            self.assertEqual(to_dict(parsed_response), to_dict(ParsedQuoteResponse))

    def test_parse_rate_parsing_error(self):
        with patch("purplship.package.mappers.canadapost.proxy.http") as mock:
            mock.return_value = QuoteParsingError
            parsed_response = rating.fetch(self.RateRequest).from_(gateway).parse()
            self.assertEqual(to_dict(parsed_response), to_dict(ParsedQuoteParsingError))

    def test_parse_rate_missing_args_error(self):
        with patch("purplship.package.mappers.canadapost.proxy.http") as mock:
            mock.return_value = QuoteMissingArgsError
            parsed_response = rating.fetch(self.RateRequest).from_(gateway).parse()
            self.assertEqual(
                to_dict(parsed_response), to_dict(ParsedQuoteMissingArgsError)
            )


if __name__ == "__main__":
    unittest.main()

RatePayload = {
    "shipper": {"postal_code": "H8Z2Z3", "country_code": "CA"},
    "recipient": {"postal_code": "H8Z2V4", "country_code": "CA"},
    "parcel": {
        "height": 3,
        "length": 10,
        "width": 3,
        "weight": 4.0,
        "dimension_unit": "CM",
        "weight_unit": "KG",
    },
    "services": ["canadapost_expedited_parcel"],
}

RateWithPresetPayload = {
    "shipper": {"postal_code": "H8Z2Z3", "country_code": "CA"},
    "recipient": {"postal_code": "H8Z2V4", "country_code": "CA"},
    "parcel": {
        "package_preset": "canadapost_xexpresspost_certified_envelope",
    },
    "services": ["canadapost_xpresspost"],
}

RateWithPresetMissingWeightPayload = {
    "shipper": {"postal_code": "H8Z2Z3", "country_code": "CA"},
    "recipient": {"postal_code": "H8Z2V4", "country_code": "CA"},
    "parcel": {
        "package_preset": "canadapost_corrugated_small_box",
    },
    "services": ["canadapost_regular_parcel"],
}

ProcessingError = [
    [],
    [
        {
            "carrier": "canadapost",
            "carrier_name": "CanadaPost",
            "code": "500",
            "message": "<parcel.weight> must be specified (required)",
        }
    ],
]

ParsedQuoteParsingError = [
    [],
    [
        {
            "carrier": "canadapost",
            "carrier_name": "CanadaPost",
            "code": "AA004",
            "message": "You cannot mail on behalf of the requested customer.",
        }
    ],
]

ParsedQuoteMissingArgsError = [
    [],
    [
        {
            "carrier": "canadapost",
            "carrier_name": "CanadaPost",
            "code": "Server",
            "message": "/rs/ship/price: cvc-particle 3.1: in element {http://www.canadapost.ca/ws/ship/rate-v4}parcel-characteristics with anonymous type, found </parcel-characteristics> (in namespace http://www.canadapost.ca/ws/ship/rate-v4), but next item should be any of [{http://www.canadapost.ca/ws/ship/rate-v4}weight, {http://www.canadapost.ca/ws/ship/rate-v4}dimensions, {http://www.canadapost.ca/ws/ship/rate-v4}unpackaged, {http://www.canadapost.ca/ws/ship/rate-v4}mailing-tube, {http://www.canadapost.ca/ws/ship/rate-v4}oversized]",
        }
    ],
]

ParsedQuoteResponse = [
    [
        {
            "base_charge": 9.59,
            "carrier": "canadapost",
            "carrier_name": "CanadaPost",
            "currency": "CAD",
            "discount": 0.62,
            "duties_and_taxes": 0.0,
            "estimated_delivery": "2011-10-24",
            "extra_charges": [
                {"amount": -0.29, "currency": "CAD", "name": "Automation discount"},
                {"amount": 0.91, "currency": "CAD", "name": "Fuel surcharge"},
            ],
            "service": "canadapost_expedited_parcel",
            "total_charge": 10.21,
        },
        {
            "base_charge": 22.64,
            "carrier": "canadapost",
            "carrier_name": "CanadaPost",
            "currency": "CAD",
            "discount": 2.56,
            "duties_and_taxes": 0.0,
            "estimated_delivery": "2011-10-21",
            "extra_charges": [
                {"amount": -0.68, "currency": "CAD", "name": "Automation discount"},
                {"amount": 3.24, "currency": "CAD", "name": "Fuel surcharge"},
            ],
            "service": "canadapost_priority",
            "total_charge": 25.2,
        },
        {
            "base_charge": 9.59,
            "carrier": "canadapost",
            "carrier_name": "CanadaPost",
            "currency": "CAD",
            "discount": 0.62,
            "duties_and_taxes": 0.0,
            "estimated_delivery": "2011-10-26",
            "extra_charges": [
                {"amount": -0.29, "currency": "CAD", "name": "Automation discount"},
                {"amount": 0.91, "currency": "CAD", "name": "Fuel surcharge"},
            ],
            "service": "canadapost_regular_parcel",
            "total_charge": 10.21,
        },
        {
            "base_charge": 12.26,
            "carrier": "canadapost",
            "carrier_name": "CanadaPost",
            "currency": "CAD",
            "discount": 1.38,
            "duties_and_taxes": 0.0,
            "estimated_delivery": "2011-10-24",
            "extra_charges": [
                {"amount": -0.37, "currency": "CAD", "name": "Automation discount"},
                {"amount": 1.75, "currency": "CAD", "name": "Fuel surcharge"},
            ],
            "service": "canadapost_xpresspost",
            "total_charge": 13.64,
        },
    ],
    [],
]


QuoteParsingError = """<messages xmlns="http://www.canadapost.ca/ws/messages">
    <message>
        <code>AA004</code>
        <description>You cannot mail on behalf of the requested customer.</description>
    </message>
</messages>
"""

QuoteMissingArgsError = """<messages xmlns="http://www.canadapost.ca/ws/messages">
    <message>
        <code>Server</code>
        <description>/rs/ship/price: cvc-particle 3.1: in element {http://www.canadapost.ca/ws/ship/rate-v4}parcel-characteristics with anonymous type, found &lt;/parcel-characteristics> (in namespace http://www.canadapost.ca/ws/ship/rate-v4), but next item should be any of [{http://www.canadapost.ca/ws/ship/rate-v4}weight, {http://www.canadapost.ca/ws/ship/rate-v4}dimensions, {http://www.canadapost.ca/ws/ship/rate-v4}unpackaged, {http://www.canadapost.ca/ws/ship/rate-v4}mailing-tube, {http://www.canadapost.ca/ws/ship/rate-v4}oversized]</description>
    </message>
</messages>
"""

RateRequestXML = f"""<mailing-scenario xmlns="http://www.canadapost.ca/ws/ship/rate-v4">
    <customer-number>2004381</customer-number>
    <expected-mailing-date>{datetime.today().strftime('%Y-%m-%d')}</expected-mailing-date>
    <parcel-characteristics>
        <weight>4.</weight>
        <dimensions>
            <length>10.</length>
            <width>3.</width>
            <height>3.</height>
        </dimensions>
    </parcel-characteristics>
    <services>
        <service-code>DOM.EP</service-code>
    </services>
    <origin-postal-code>H8Z2Z3</origin-postal-code>
    <destination>
        <domestic>
            <postal-code>H8Z2V4</postal-code>
        </domestic>
    </destination>
</mailing-scenario>
"""

RateRequestUsingPackagePresetXML = f"""<mailing-scenario xmlns="http://www.canadapost.ca/ws/ship/rate-v4">
    <customer-number>2004381</customer-number>
    <expected-mailing-date>{datetime.today().strftime('%Y-%m-%d')}</expected-mailing-date>
    <parcel-characteristics>
        <weight>0.5</weight>
        <dimensions>
            <width>26.</width>
            <height>15.9</height>
        </dimensions>
    </parcel-characteristics>
    <services>
        <service-code>DOM.XP</service-code>
    </services>
    <origin-postal-code>H8Z2Z3</origin-postal-code>
    <destination>
        <domestic>
            <postal-code>H8Z2V4</postal-code>
        </domestic>
    </destination>
</mailing-scenario>
"""

RateResponseXml = """<price-quotes>
   <price-quote>
      <service-code>DOM.EP</service-code>
      <service-link rel="service" href="https://ct.soa-gw.canadapost.ca/rs/ship/service/DOM.EP?country=CA" media-type="application/vnd.cpc.ship.rate-v4+xml" />
      <service-name>Expedited Parcel</service-name>
      <price-details>
         <base>9.59</base>
         <taxes>
            <gst>0.00</gst>
            <pst>0</pst>
            <hst>0</hst>
         </taxes>
         <due>10.21</due>
         <options>
            <option>
               <option-code>DC</option-code>
               <option-name>Delivery confirmation</option-name>
               <option-price>0</option-price>
            </option>
         </options>
         <adjustments>
            <adjustment>
               <adjustment-code>AUTDISC</adjustment-code>
               <adjustment-name>Automation discount</adjustment-name>
               <adjustment-cost>-0.29</adjustment-cost>
               <qualifier>
                  <percent>3.000</percent>
               </qualifier>
            </adjustment>
            <adjustment>
               <adjustment-code>FUELSC</adjustment-code>
               <adjustment-name>Fuel surcharge</adjustment-name>
               <adjustment-cost>0.91</adjustment-cost>
               <qualifier>
                  <percent>9.75</percent>
               </qualifier>
            </adjustment>
         </adjustments>
      </price-details>
      <weight-details />
      <service-standard>
         <am-delivery>false</am-delivery>
         <guaranteed-delivery>true</guaranteed-delivery>
         <expected-transit-time>2</expected-transit-time>
         <expected-delivery-date>2011-10-24</expected-delivery-date>
      </service-standard>
   </price-quote>
   <price-quote>
      <service-code>DOM.PC</service-code>
      <service-link rel="service" href="https://ct.soa-gw.canadapost.ca/rs/ship/service/DOM.PC?country=CA" media-type="application/vnd.cpc.ship.rate-v4+xml" />
      <service-name>Priority Courier</service-name>
      <price-details>
         <base>22.64</base>
         <taxes>
            <gst>0.00</gst>
            <pst>0</pst>
            <hst>0</hst>
         </taxes>
         <due>25.20</due>
         <options>
            <option>
               <option-code>DC</option-code>
               <option-name>Delivery confirmation</option-name>
               <option-price>0</option-price>
            </option>
         </options>
         <adjustments>
            <adjustment>
               <adjustment-code>AUTDISC</adjustment-code>
               <adjustment-name>Automation discount</adjustment-name>
               <adjustment-cost>-0.68</adjustment-cost>
               <qualifier>
                  <percent>3.000</percent>
               </qualifier>
            </adjustment>
            <adjustment>
               <adjustment-code>FUELSC</adjustment-code>
               <adjustment-name>Fuel surcharge</adjustment-name>
               <adjustment-cost>3.24</adjustment-cost>
               <qualifier>
                  <percent>14.75</percent>
               </qualifier>
            </adjustment>
         </adjustments>
      </price-details>
      <weight-details />
      <service-standard>
         <am-delivery>false</am-delivery>
         <guaranteed-delivery>true</guaranteed-delivery>
         <expected-transit-time>1</expected-transit-time>
         <expected-delivery-date>2011-10-21</expected-delivery-date>
      </service-standard>
   </price-quote>
   <price-quote>
      <service-code>DOM.RP</service-code>
      <service-link rel="service" href="https://ct.soa-gw.canadapost.ca/rs/ship/service/DOM.RP?country=CA" media-type="application/vnd.cpc.ship.rate-v4+xml" />
      <service-name>Regular Parcel</service-name>
      <price-details>
         <base>9.59</base>
         <taxes>
            <gst>0.00</gst>
            <pst>0</pst>
            <hst>0</hst>
         </taxes>
         <due>10.21</due>
         <options>
            <option>
               <option-code>DC</option-code>
               <option-name>Delivery confirmation</option-name>
               <option-price>0</option-price>
               <qualifier>
                  <included>true</included>
               </qualifier>
            </option>
         </options>
         <adjustments>
            <adjustment>
               <adjustment-code>AUTDISC</adjustment-code>
               <adjustment-name>Automation discount</adjustment-name>
               <adjustment-cost>-0.29</adjustment-cost>
               <qualifier>
                  <percent>3.000</percent>
               </qualifier>
            </adjustment>
            <adjustment>
               <adjustment-code>FUELSC</adjustment-code>
               <adjustment-name>Fuel surcharge</adjustment-name>
               <adjustment-cost>0.91</adjustment-cost>
               <qualifier>
                  <percent>9.75</percent>
               </qualifier>
            </adjustment>
         </adjustments>
      </price-details>
      <weight-details />
      <service-standard>
         <am-delivery>false</am-delivery>
         <guaranteed-delivery>false</guaranteed-delivery>
         <expected-transit-time>4</expected-transit-time>
         <expected-delivery-date>2011-10-26</expected-delivery-date>
      </service-standard>
   </price-quote>
   <price-quote>
      <service-code>DOM.XP</service-code>
      <service-link rel="service" href="https://ct.soa-gw.canadapost.ca/rs/ship/service/DOM.XP?country=CA" media-type="application/vnd.cpc.ship.rate-v4+xml" />
      <service-name>Xpresspost</service-name>
      <price-details>
         <base>12.26</base>
         <taxes>
            <gst>0.00</gst>
            <pst>0</pst>
            <hst>0</hst>
         </taxes>
         <due>13.64</due>
         <options>
            <option>
               <option-code>DC</option-code>
               <option-name>Delivery confirmation</option-name>
               <option-price>0</option-price>
            </option>
         </options>
         <adjustments>
            <adjustment>
               <adjustment-code>AUTDISC</adjustment-code>
               <adjustment-name>Automation discount</adjustment-name>
               <adjustment-cost>-0.37</adjustment-cost>
               <qualifier>
                  <percent>3.000</percent>
               </qualifier>
            </adjustment>
            <adjustment>
               <adjustment-code>FUELSC</adjustment-code>
               <adjustment-name>Fuel surcharge</adjustment-name>
               <adjustment-cost>1.75</adjustment-cost>
               <qualifier>
                  <percent>14.75</percent>
               </qualifier>
            </adjustment>
         </adjustments>
      </price-details>
      <weight-details />
      <service-standard>
         <am-delivery>false</am-delivery>
         <guaranteed-delivery>true</guaranteed-delivery>
         <expected-transit-time>2</expected-transit-time>
         <expected-delivery-date>2011-10-24</expected-delivery-date>
      </service-standard>
   </price-quote>
</price-quotes>
"""
