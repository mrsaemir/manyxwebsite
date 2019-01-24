from django.test import LiveServerTestCase
from rest_framework.test import APIClient
import requests
from django.contrib.auth import get_user_model


# testing the main page for blog; testing availability of the main page.
class TestBlogMainPage(LiveServerTestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username="admin", is_superuser=True, is_staff=True)
        user.set_password("adminadmin")
        user.save()
        res = requests.post(self.live_server_url + '/api/token/',
                            data={"username": "admin", "password": "adminadmin"}).json()
        self.token = res['token']

    def test_availability_for_main_page(self):
        client = APIClient()
        res = client.get(self.live_server_url + '/blog/')
        self.assertEqual(res.status_code, 200, "Blog page is not available.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, HEAD, OPTIONS", "Blog has wrong allow options.")
        self.assertEqual(res.json(), [], "Blog is returning bad json response.")

    def test_main_page_shows_stuff(self):
        self.fail("write me")

    def test_availability_for_admin_page(self):
        client = APIClient()
        res = client.get(self.live_server_url + '/blog/admin/')
        self.assertNotEqual(res.status_code, 404, "Blog admin page is not available.")
        # checking permissions working properly.
        self.assertEqual(res.status_code, 401, "permissions are not working properly.")
        # lets log into admin page for blog
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        res = client.get(path=self.live_server_url + '/blog/admin/')
        self.assertEqual(res.status_code, 200, "Can't log into blog's admin page.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog admin page is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, POST, HEAD, OPTIONS", "Blog admin page has wrong allow options.")
        # check data
        self.assertEqual(res.json(), [], "Blog admin page is returning bad json response.")

    def test_admin_page_adds_and_shows_stuff(self):
        # also check for unpublished stuff
        self.fail("write me")

    def test_modification_works(self):
        self.fail("write me")

    def test_anonymous_cant_modify(self):
        self.fail("write me")
