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

    def create_valid_post_as_staff_user(self, title="blog title", text="lorem ipsum is comming to be saved",
                                        publication_datetime="", slug=""):
        client = self.staff_client
        data = {"title": title, "text": text,
                "publication_datetime": publication_datetime, "slug": slug}
        res = client.post(self.live_server_url + "/blog/admin/", data=data, format='json')
        self.assertEqual(res.status_code, 201, "can't post data to /blog/admin/")

    def create_valid_post_as_admin_user(self, title="blog title2", text="lorem ipsum is comming to be saved here",
                                        publication_datetime="", slug=""):
        client = self.admin_client
        data = {"title": title, "text": text,
                "publication_datetime": publication_datetime, "slug": slug}
        res = client.post(self.live_server_url + "/blog/admin/", data=data, format='json')
        self.assertEqual(res.status_code, 201, "can't post data to /blog/admin/")

    def test_availability_for_main_page(self):
        client = APIClient()
        res = client.get(self.live_server_url + '/blog/')
        self.assertEqual(res.status_code, 200, "Blog page is not available.")
        # check headers
        self.assertEqual(res["Content-Type"], "application/json", "Blog is returning wrong content type.")
        self.assertEqual(res['allow'], "GET, HEAD, OPTIONS", "Blog has wrong allow options.")
        self.assertEqual(res.json(), [], "Blog is returning bad json response.")

    def test_main_page_shows_stuff(self):
        self.create_valid_post_as_staff_user(publication_datetime="1390-05-06 12:20")
        # assure that post shows up.
        client = APIClient()
        res = client.get(self.live_server_url + "/blog/")
        self.assertEqual(res.status_code, 200, "can't retrieve blog posts")
        self.assertEqual(res.json(), [{'title': 'blog title', 'slug': 'blog-title',
                                       'auther': {'auther': 'staff', 'link': 'http://testserver/manyx/staff/'},
                                       'publication_datetime': '1390-5-6 12:20', 'likes': 0, 'tags': None,
                                       'text': 'lorem ipsum is comming to be saved'}])
        # testing the second item.
        self.create_valid_post_as_admin_user(publication_datetime="1390-05-06 12:20")
        res = client.get(self.live_server_url + "/blog/")
        self.assertEqual(res.status_code, 200, "can't retrieve blog posts")
        self.assertEqual(res.json(), [{'title': 'blog title', 'slug': 'blog-title',
                                       'auther': {'auther': 'staff', 'link': 'http://testserver/manyx/staff/'},
                                       'publication_datetime': '1390-5-6 12:20', 'likes': 0, 'tags': None,
                                       'text': 'lorem ipsum is comming to be saved'},
                                      {'title': 'blog title2', 'slug': 'blog-title2',
                                       'auther': {'auther': 'admin', 'link': 'http://testserver/manyx/admin/'},
                                       'publication_datetime': '1390-5-6 12:20', 'likes': 0, 'tags': None,
                                       'text': 'lorem ipsum is comming to be saved here'}])

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

    # scenario: you just delete publication datetime and a new one should be generated and set to now.
    def test_publication_datetime_works_on_edit(self):
        self.fail("write me")

    # scenario: you just delete slug and a new one should be created.
    def test_slug_works_on_delete(self):
        self.fail("write me")

    # you enter an invalid slug and it returns error. and then you enter the correct one and it works.
    def test_slug_works_on_modify(self):
        self.fail("write me")

    def test_each_person_can_only_edit_his_own_post(self):
        self.fail("write me")

    def test_admin_can_delete_a_post(self):
        self.fail("write me")

    # scenario: a staff user tries to delete somebody else's data and she can't then she tries to delete her data
    # and she succeeds.
    def test_staff_can_delete_their_own_posts(self):
        self.fail("write me")

    def test_admin_can_edit_anything(self):
        self.fail("write me")

    def test_modification_works(self):
        self.fail("write me")

    def test_anonymous_cant_modify(self):
        self.fail("write me")

    def test_anonymous_cant_create(self):
        self.fail("write me")

    def test_tags(self):
        self.fail("write me")

    def test_duplicate_titles_arent_saved(self):
        self.fail("write me")

    def test_duplicate_slugs_arent_saved(self):
        self.fail("write me")

    def test_publication_datetime_auto_creation(self):
        self.fail("write me")

    def test_slug_auto_creation(self):
        self.fail("write me")

    def test_main_page_does_now_show_unpublished_posts(self):
        self.fail("write me")

    def test_main_page_shows_unpublished_items_when_is_the_time(self):
        self.fail("write me")

    # scenario: one time send as staff and one time send as admin
    def test_correct_auther_is_set_to_each_post(self):
        self.fail("write me")

    def test_likes_dislikes_and_reports_are_zero_on_creation(self):
        self.fail("write me")

    def test_modifying_created_and_last_modification_is_limited(self):
        self.fail("write me")
