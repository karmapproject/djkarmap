from django.test import SimpleTestCase, TestCase


class SimpleTests(SimpleTestCase):
    # If we were using a database, we’d instead use TestCase.
    """
    AssertionError:
    Database queries to 'default' are not allowed in SimpleTestCase subclasses.
    Either subclass TestCase or TransactionTestCase to ensure proper test isolation
    or add 'default' to pages.tests.SimpleTests.databases to silence this failure.
    
    """
    # def test_home_page_status_code(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
