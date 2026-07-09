from django.test import SimpleTestCase

from karrio.server.graph.schemas.base.types import MessageType


class TestMessageTypeParse(SimpleTestCase):
    def test_parse_message_without_code(self):
        """Regression: carrier messages may omit code (e.g. freightcom_rest rate errors)."""
        msg = {
            "level": "error",
            "message": "bad or missing data",
            "carrier_id": "freightcomRest",
            "carrier_name": "freightcom_rest",
            "details": {"field": "hsverified"},
        }

        parsed = MessageType.parse(msg)

        self.assertIsNone(parsed.code)
        self.assertEqual(parsed.message, "bad or missing data")
        self.assertEqual(parsed.carrier_id, "freightcomRest")

    def test_parse_message_with_all_fields(self):
        msg = {
            "code": "customs_error",
            "message": "invalid customs",
            "carrier_id": "ups",
            "carrier_name": "ups",
            "details": None,
        }

        parsed = MessageType.parse(msg)

        self.assertEqual(parsed.code, "customs_error")
        self.assertEqual(parsed.carrier_name, "ups")
