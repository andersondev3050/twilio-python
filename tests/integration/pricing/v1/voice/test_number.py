# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class NumberTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.pricing.v1.voice \
                                  .numbers(number="+987654321").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://pricing.twilio.com/v1/Voice/Numbers/+987654321',
        ))
