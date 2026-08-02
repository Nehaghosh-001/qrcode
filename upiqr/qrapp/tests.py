from django.test import TestCase, Client


class UPIQRAppTests(TestCase):
    def test_home_page_get_returns_200(self):
        response = Client().get('/', HTTP_HOST='127.0.0.1')
        self.assertEqual(response.status_code, 200)

    def test_home_page_post_returns_qr_for_valid_upi(self):
        response = Client().post('/', {'contact': 'test@upi'}, HTTP_HOST='127.0.0.1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your QR Code')

    def test_home_page_post_returns_error_for_invalid_upi(self):
        response = Client().post('/', {'contact': '9876543210'}, HTTP_HOST='127.0.0.1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a valid UPI ID.')
