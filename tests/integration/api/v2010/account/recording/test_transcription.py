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


class TranscriptionTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .transcriptions(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .transcriptions(sid="TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_read_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.twilio.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .transcriptions.read()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json',
        ))
