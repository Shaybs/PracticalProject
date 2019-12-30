from application import app
import unittest

class TestCase(TestCase):

	#Test the HTTP response for the account page
	def  test_home_view(self):
		response = self.client.get(url_for('test_account'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the country page
	def  test_home_view(self):
		response = self.client.get(url_for('test_country'))
		self.assertEqual(response.status_code, 200)
