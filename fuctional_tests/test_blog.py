from django.test import LiveServerTestCase, Client


# testing the main page for blog; testing availability of the main page.
class TestBlogMainPage(LiveServerTestCase):

    def test_availability_for_main_page(self):
        client = Client()
        res = client.get(self.live_server_url + '/blog/')
        self.assertEqual(res.status_code, 200, "Blog page is not available.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, HEAD, OPTIONS", "Blog has wrong allow options.")
        self.assertEqual(res.json(), [], "Blog is returning bad json response.")

