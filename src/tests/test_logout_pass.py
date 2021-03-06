import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app
from blueprint_test_case import BaseTestCase

class FlaskTestCase(BaseTestCase):

    # Ensure login behaves correctly with correct credentials
    def test_correct_customer_login(self):
        # login as that user
        response = self.client.post(
            '/login/vendor',
            data = dict(username="testing", password="testing")
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful!', response.data)

        # then logout
        response = self.client.get(
            '/logout'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(u'"You logged out!', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_vendor_login(self):
        # login as that user
        response = self.client.post(
            '/login/customer',
            data = dict(username="testing", password="testing")
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login successful!', response.data)

        # then logout
        response = self.client.get(
            '/logout'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(u'"You logged out!', response.data)