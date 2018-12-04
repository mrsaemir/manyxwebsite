import requests
from bs4 import BeautifulSoup
from datetime import datetime
import jdatetime
from pytz import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.db.utils import IntegrityError
from django.db import transaction
from blog.models import Blog
ManyxUser = get_user_model()


# a function that gets time from a site on the internet and returns jalali datetime equivalent
def get_clock_from_outside():
    # By Mehdi Sorkhe Miri
    res = requests.get("https://www.unixtimestamp.com/index.php").text
    soup = BeautifulSoup(res, 'lxml')
    timetag = soup.find("h3", class_="text-danger")
    st = timetag.find("small").decompose()
    timestamp = int(timetag.text.strip())
    # By Amirhossein Saemi
    gregorian = datetime.fromtimestamp(timestamp).replace(tzinfo=timezone("Asia/Tehran"))
    jalali = jdatetime.datetime.fromgregorian(datetime=gregorian)
    return jalali


# each blog will have three timing plans: creation_date_and_time,
# publication_date_and_time, last_modify_date_and_time
class ManyxBlogModelTest(TestCase):
    def setUp(self):
        self.ipsum = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
         Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown 
         printer took a galley of type and scrambled it to make a type specimen book. It has survived not 
         only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
         It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
         and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

    def test_saving_and_retrieving_items(self):
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="manyx is coming", text=self.ipsum, auther=auther)

        blog_posts = Blog.objects.count()
        self.assertEqual(blog_posts, 1)

        first_post = Blog.objects.first()
        self.assertEqual(first_post.title, "manyx is coming")
        self.assertEqual(first_post.text, self.ipsum)
        self.assertEqual(first_post.auther, auther)

        Blog.objects.create(title="manyx has come", text="say hello to manyx", auther=auther)

        blog_posts = Blog.objects.count()
        self.assertEqual(blog_posts, 2)

    def test_title_uniqueness(self):
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="title1", text=self.ipsum, auther=auther,
                            slug=slugify("different-slug"))
        first = Blog.objects.first()
        try:
            with transaction.atomic():
                Blog.objects.create(title=first.title, text=self.ipsum, auther=auther)
            self.fail("Title uniqueness is violated.")
        except IntegrityError:
            # title uniqueness is not violated.
            pass

    def test_slug_uniqueness(self):
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="title1", text=self.ipsum, auther=auther)
        first = Blog.objects.first()
        try:
            with transaction.atomic():
                Blog.objects.create(title="title2", text=self.ipsum, auther=auther,
                                    slug=first.slug)
            self.fail("Slug uniqueness is violated.")
        except IntegrityError:
            # slug uniqueness is fine.
            pass

    def test_auto_slug_creation(self):
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="بزودی شاهد خواهیم بود.", text=self.ipsum, auther=auther)

        first_post = Blog.objects.first()
        self.assertEqual(first_post.slug, "بزودی-شاهد-خواهیم-بود")

        # set slug function does not save slug itself.
        first_post.slug = slugify("اکنون-شاهدش-هستیم", allow_unicode=True)
        first_post.save()

        first_post = Blog.objects.first()
        self.assertEqual(first_post.slug, "اکنون-شاهدش-هستیم")

    def test_blog_post_creation_datetime(self):
        # publication_datetime, creation_datetime, and last_modify_datetime should be checked
        # by default publication_date is creation_date
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="some title", text=self.ipsum, auther=auther)

        # check creation_date
        blog_post = Blog.objects.first()
        self.assertNotEqual(blog_post.creation_datetime, None)
        # check type
        self.assertEqual(type(blog_post.creation_datetime), jdatetime.datetime)
        # check that date time is correct.
        self.assertEqual(blog_post.creation_datetime.strftime("%b %d %Y %H:%M"),
                         get_clock_from_outside().strftime("%b %d %Y %H:%M"))

    def test_blog_post_last_modified_datetime(self):
        import time
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="some title", text=self.ipsum, auther=auther)

        blog_post = Blog.objects.first()
        self.assertNotEqual(blog_post.last_modified_datetime, None)
        self.assertEqual(type(blog_post.last_modified_datetime), jdatetime.datetime)
        last_modified = blog_post.last_modified_datetime
        self.assertEqual(blog_post.creation_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                         last_modified.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(2)
        blog_post.title = "some new title"
        blog_post.save()

        # check that last modified datetime is changed after edit
        blog_post = Blog.objects.first()
        self.assertNotEqual(blog_post.last_modified_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            last_modified.strftime("%Y-%m-%d %H:%M:%S"))

    def test_blog_post_publication_datetime(self):
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="some title", text=self.ipsum, auther=auther)

        blog_post = Blog.objects.first()

        import jdatetime
        jalali_datetime = jdatetime.datetime.now()
        self.assertEqual(jalali_datetime.strftime("%Y %M %D - %H:%M"),
                         get_clock_from_outside().strftime("%Y %M %D - %H:%M"))
        blog_post.publication_datetime = jalali_datetime
        blog_post.save()

        blog_post = Blog.objects.first()
        self.assertEqual(blog_post.publication_datetime, jalali_datetime)

    def test_blog_post_likes_dislikes_views_and_reports(self):
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="some title", text=self.ipsum, auther=auther)

        blog_post = Blog.objects.first()
        # first initialization check
        self.assertEqual(blog_post.likes, 0)
        self.assertEqual(blog_post.dislikes, 0)
        self.assertEqual(blog_post.reports, 0)

        # check them to accept positive integers only
        # likes
        try:
            with transaction.atomic():
                blog_post.likes = -1
                blog_post.save()
            self.fail("Likes are accepting negative numbers. they should always be positive.")
        except IntegrityError:
            pass
        blog_post = Blog.objects.first()
        # dislikes
        try:
            with transaction.atomic():
                blog_post.dislikes = -1
                blog_post.save()
            self.fail("Dislikes are accepting negative numbers. they should always be positive.")
        except IntegrityError:
            pass
        blog_post = Blog.objects.first()
        # reports
        try:
            with transaction.atomic():
                blog_post.reports = -1
                blog_post.save()
            self.fail("Reports are accepting negative numbers. they should always be positive.")
        except IntegrityError:
            pass

    def test_blog_post_tags(self):
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="some title", text=self.ipsum, auther=auther)

        blog_post = Blog.objects.first()
        self.assertEqual(blog_post.tags, None)

        # adding a new one
        import json
        tags = ["action", "manyxy", "blog", "tech"]
        tags = json.dumps(tags)
        blog_post.tags = tags
        blog_post.save()

        # fetching and checking
        blog_post = Blog.objects.first()
        self.assertEqual(blog_post.tags, tags)

    def test_is_published(self):
        # publish works with comparing puclication_datetime with now datetime
        # if now datetime is greater than publication datetime, then the post
        # is published
        auther = ManyxUser.objects.create(username="admin")
        Blog.objects.create(title="some title", text=self.ipsum, auther=auther)

        # each post is published at creation time by default.
        blog_post = Blog.published.first()
        self.assertTrue(blog_post)
        blog_post.publication_datetime = jdatetime.datetime(year=1800,
                                                            month=10, day=25)
        blog_post.save()
        blog_post = Blog.published.first()
        self.assertFalse(blog_post)



