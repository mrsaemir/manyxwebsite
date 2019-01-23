from django.test import LiveServerTestCase
from rest_framework.test import APIClient


# testing the main page for blog; testing availability of the main page.
class TestBlogMainPage(LiveServerTestCase):
    def test_availability_for_main_page(self):
        client = APIClient()
        res = client.get(self.live_server_url + '/blog/')
        self.assertEqual(res.status_code, 200, "Blog page is not available.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, HEAD, OPTIONS", "Blog has wrong allow options.")
        self.assertEqual(res.json(), [], "Blog is returning bad json response.")

    def test_availability_for_admin_page(self):
        client = APIClient()
        res = client.get(self.live_server_url + '/blog/admin/')
        self.assertNotEqual(res.status_code, 404, "Blog admin page is not available.")
        # checking permissions working properly.
        self.assertEqual(res.status_code, 401, "permissions are not working properly.")
