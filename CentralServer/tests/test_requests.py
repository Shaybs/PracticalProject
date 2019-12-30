from application import app
import unittest

class Test_Responses(TestCase):

	#Test the random number generation
	def test_post_account_1(self):
		response = self.client.get(url_for('test_account'))
		self.assertEqual(response.count(), 1)

	#Test the random number generation
	def test_post_account_1(self):
		response = self.client.get(url_for('test_account_6'))
		self.assertEqual(response.count(), 6)

	#Test the random number generation
	def test_post_account_1(self):
		response = self.client.get(url_for('test_account_8'))
		self.assertEqual(response.count(), 8)

	#Test the random character generation
	def test_post_account_1(self):
		response = self.client.get(url_for('test_country'))
		self.assertEqual(response.count(), 1)

	#Test the random character generation
	def test_post_account_6(self):
		response = self.client.get(url_for('test_country_4'))
		self.assertEqual(response.count(), 4)

	#Test the random character generation
	def test_post_account_8(self):
		response = self.client.get(url_for('test_country_8'))
		self.assertEqual(response.count(), 8)

	#Test IBAN generation
	def test_iban(self):
		response = self.client.get(url_for('test_iban'))
		self.assertEqual(response.count(), 34)

if __name__ == '__main__':
	unittest.main()

#One test for the length of Account number
#One test for the peamble of the IBAN
#One test for the length IBAN string
#One test for sending information from the CentralServer to the AccountGenerator
#One test for recieving infromation from the AccountGenerator
#One test for send information from the Central Server to the CountryGenerator
#One test for recieving information from the CountryGenerator
#One test for send information from the Central Server to the FrontEnd
#One test for recieving information from the FrontEnd