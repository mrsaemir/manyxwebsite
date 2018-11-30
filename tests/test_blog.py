from django.test import LiveServerTestCase, Client


# VERY IMPORTANT : test datetimes to be correct in iran.

# testing the main page for blog; testing availability of the main page.
class TestBlogMainPage(LiveServerTestCase):
    # check that browsable api renderer is not activated in REST_FRAMEWORK_SETTINGS.
    def test_renderer_settings(self):
        from django.conf import settings
        RENDERER_CLASSES = ('rest_framework.renderers.JSONRenderer',)
        self.assertTupleEqual(
                         settings.REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'],
                         RENDERER_CLASSES,
                         "Wrong configuration for DEFAULT RENDERER CLASSES")

    def test_availability_for_main_page(self):
        client = Client()
        res = client.get(self.live_server_url + '/blog/')
        self.assertEqual(res.status_code, 200, "Blog page is not available.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, HEAD, OPTIONS", "Blog has wrong allow options.")
        self.assertEqual(res.json(), [], "Blog is returning bad json response.")
