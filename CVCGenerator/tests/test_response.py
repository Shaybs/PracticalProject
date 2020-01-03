from application import app
import unittest

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