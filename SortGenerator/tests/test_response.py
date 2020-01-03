from application import app
import unittest

class Test_Responses(TestCase):

	#Test the HTTP response for the account page
	def  test_post_account_view(self):
		response = self.client.get(url_for('post-sort'))
		self.assertEqual(response.status_code, 200)

	#Test that there are 8 characters generation
	def test_post_account_8(self):
		response = self.client.get(url_for('post-sort'))
		self.assertEqual(response.count(), 8)

if __name__ == '__main__':
	unittest.main()
