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

#One test for whether the Account number is made only integers
#One test for the length of Account number
#One test for the peamble of the IBAN
#One test for the length IBAN string
#One test for sending information from the CentralServer to the AccountGenerator
#One test for recieving infromation from the AccountGnerator
#One test for send information from the Central Server to the CountryGenerator
#One test for recieving information from the CountryGenerator
#One test for send information from the Central Server to the FrontEnd
#One test for recieving information from the FrontEnd