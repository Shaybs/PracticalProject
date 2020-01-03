from application import app
import unittest

class Test_Responses(TestCase):

	#Test the HTTP response for the account page
	def  test_post_account_view(self):
		response = self.client.get(url_for('post-cardnumber'))
		self.assertEqual(response.status_code, 200)

	#Test the random number generation
	def test_post_account_1(self):
		response = self.client.get(url_for('post-cardnumber'))
		self.assertEqual(response.count(), 16)

if __name__ == '__main__':
	unittest.main()