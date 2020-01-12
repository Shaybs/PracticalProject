from application import app
import unittest
from flask_testing import TestCase
import requests
from unittest import mock


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code 

        def json(self):
            return self.json_data

    if args[0] == 'http://cvc-service:5006/post-cvc/':
    	return MockResponse({"CVC": "343"}, 200)

    return MockResponse(None, 404)

class ResponseTestClass(unittest.TestCase):
	@mock.patch('requests.get', side_effect=mocked_requests_get)
	def test_PK(self, mock_get):
		#Assert requests.get calls
		ibanPK = requests.get('http://cvc-service:5006/post-iban-PK/').json()
		self.assertEqual(ibanPK, {"CVC": "343"})

class Test_Responses(TestCase):

	#Test the HTTP response for the account page
	def  test_post_account_view(self):
		response = self.client.get(url_for('post-cvc'))
		self.assertEqual(response.status_code, 200)

	#Test there are 3 random characters generation
	def test_post_account_6(self):
		response = self.client.get(url_for('post-cvc'))
		self.assertEqual(response.count(), 3)

if __name__ == '__main__':
	unittest.main()