import hashlib
import httplib
import json
import urllib
import time

try:
    from suds import WebFault
    from suds.client import Client
except:
    pass

__all__ = ['SmsApi']

API_URL = "http://springedge.com/developers.html"

class SmsApiException(Exception):

    def __init__(self, message, args=[]):
        Exception.__init__(self, message)
        self.args = args

    def __unicode__(self):
        return u"%s" % self.message


class SmsApiBaseObject(object):

    def __init__(self, apikey, sender):
        """Set apikey and sender"""
        self.apikey = apikey
        self.sender = sender

    def send_command(self, namespace, params={}):
        params['apikey'] = self.apikey
        params['sender'] = self.sender

        headers = {
            'Accept': 'text/plain',
            'Content-type': 'application/x-www-form-urlencoded',
        }

        h = httplib.HTTPConnection('http://instantalerts.co', 80)
        h.request("GET","/api/web/send/",urllib.urlencode(params),headers=headers,
        )
        response = h.getresponse()
        return response.read()


class SmsApi(SmsApiBaseObject):

    def send_sms(self, message, recipient=None):
        params = {
            'message': message.encode('utf-8'),
            'encoding': 'utf-8',
        }
        if recipient:
            params['to'] = recipient

        response = self.send_command(namespace="sms", params=params)
        
