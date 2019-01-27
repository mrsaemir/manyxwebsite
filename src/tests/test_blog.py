import json
from django.test import LiveServerTestCase
from rest_framework.test import APIClient
import requests
from django.contrib.auth import get_user_model
User = get_user_model()


# testing the main page for blog; testing availability of the main page.
class TestBlogMainPage(LiveServerTestCase):
    # creating both staff and admin users.
    def setUp(self):
        admin_user = User.objects.create(username="admin", is_superuser=True, is_staff=True)
        admin_user.set_password("adminadmin")
        admin_user.save()
        self.admin_user = admin_user
        res = requests.post(self.live_server_url + '/api/token/',
                            data={"username": "admin", "password": "adminadmin"}).json()
        self.admin_token = res['token']
        self.admin_client = APIClient()
        self.admin_client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token)

        # creating staff user.
        staff_user = User.objects.create(username="staff", is_staff=True)
        staff_user.set_password("staffstaff")
        staff_user.save()
        self.staff_user = staff_user
        res = requests.post(self.live_server_url + '/api/token/',
                            data={"username": "staff", "password": "staffstaff"}).json()
        self.staff_token = res['token']
        self.staff_client = APIClient()
        self.staff_client.credentials(HTTP_AUTHORIZATION='Token ' + self.staff_token)

    def create_valid_post_as_staff_user(self):
        client = self.staff_client
        data = {"title": "blog title", "text": "lorem ipsum is comming to be saved",
                "publication_datetime": "1390-05-06 12:20", "slug": ""}

        res = client.post(self.live_server_url + "/blog/admin/", data=data, format='json')
        self.assertEqual(res.status_code, 201, "can't post data to /blog/admin/")

    def create_valid_post_as_admin_user(self):
        self.fail("write me")

    def test_availability_for_main_page(self):
        client = APIClient()
        res = client.get(self.live_server_url + '/blog/')
        self.assertEqual(res.status_code, 200, "Blog page is not available.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, HEAD, OPTIONS", "Blog has wrong allow options.")
        self.assertEqual(res.json(), [], "Blog is returning bad json response.")

    def test_main_page_shows_stuff(self):
        self.create_valid_post_as_staff_user()
        # assure that post shows up.
        client = APIClient()
        res = client.get(self.live_server_url + "/blog/")
        self.assertEqual(res.json(), [{'title': 'blog title', 'slug': 'blog-title',
                                       'auther': {'auther': 'staff', 'link': 'http://testserver/manyx/staff/'},
                                       'publication_datetime': '1390-5-6 12:20', 'likes': 0, 'tags': None,
                                       'text': 'lorem ipsum is comming to be saved'}])

    def test_availability_for_admin_page(self):
        client = APIClient()
        res = client.get(self.live_server_url + '/blog/admin/')
        self.assertNotEqual(res.status_code, 404, "Blog admin page is not available.")
        # checking permissions working properly.
        self.assertEqual(res.status_code, 401, "permissions are not working properly.")
        # lets log into admin page for blog
        client = self.admin_client
        res = client.get(path=self.live_server_url + '/blog/admin/')
        self.assertEqual(res.status_code, 200, "Can't log into blog's admin page.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog admin page is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, POST, HEAD, OPTIONS", "Blog admin page has wrong allow options.")
        # check data
        self.assertEqual(res.json(), [], "Blog admin page is returning bad json response.")

    def test_admin_page_adds_and_shows_stuff(self):
        # also check for unpublished stuff
        self.create_valid_post_as_staff_user()
        self.fail("write me")

    def test_modification_works(self):
        self.fail("write me")

    def test_anonymous_cant_modify(self):
        self.fail("write me")
