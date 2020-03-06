from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    # If we were using a database, we’d instead use TestCase.
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
