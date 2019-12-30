from application import app
import unittest

class Test_Responses(TestCase):

	#Test the HTTP response for the account page
	def  test_post_account_view(self):
		response = self.client.get(url_for('get_test'))
		self.assertEqual(response.status_code, 200)

	#Test the random number generation
	def test_post_account_1(self):
		response = self.client.get(url_for('post_test'))
		self.assertEqual(response.count(), 1)

	#Test the random number generation
	def test_post_account_6(self):
		response = self.client.get(url_for('post_test_4'))
		self.assertEqual(response.count(), 4)

	#Test the random number generation
	def test_post_account_8(self):
		response = self.client.get(url_for('post_test_8'))
		self.assertEqual(response.count(), 8)

if __name__ == '__main__':
	unittest.main()


#Is it successfully connecting to the central server
#Is it recieving an object
#Is it generating a pre-amble for the IBAN
#Is it generating 4 random characters?
#Is it generating 8 random characters
#Are the characters being sent to the central server?