from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.db.utils import IntegrityError
from django.db import transaction
import jdatetime
from blog.models import Blog
ManyxUser = get_user_model()


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
        # check types
        self.assertEqual(type(blog_post.creation_datetime), jdatetime.datetime)
        now = jdatetime.datetime.now()
        now_date_time = "{}/{}/{} - {}:{}".format(now.year,
                                                  now.month,
                                                  now.day,
                                                  now.hour,
                                                  now.minute)
        creation_date_time = "{}/{}/{} - {}:{}".format(blog_post.creation_datetime.year,
                                                       blog_post.creation_datetime.month,
                                                       blog_post.creation_datetime.day,
                                                       blog_post.creation_datetime.hour,
                                                       blog_post.creation_datetime.minute)
        self.assertEqual(creation_date_time, now_date_time)

    def test_blog_post_last_modified_datetime(self):
        pass

    def test_blog_post_publication_datetime(self):
        pass

    def test_blog_post_likes_dislikes_views_and_reports(self):
        pass

    def test_blog_post_tags(self):
        pass

