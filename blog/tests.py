from django.test import TestCase
from .models import Blog
from manyx.manyx.models import ManyxUser
import jdatetime


# each blog will have three timing plans: creation_date_and_time,
# publication_date_and_time, last_modify_date_and_time
class ManyxBlogModelTest(TestCase):
    def setUp(self):
        # a user for testing foreign keys.
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
        self.assertEqual(first_post.title, "manyx is comint")
        self.assertEqual(first_post.text, self.ipsum)
        self.assertEqual(first_post.auther, auther)

        Blog.objects.create(title="manyx has come", text="say hello to manyx", auther=auther)

        blog_posts = Blog.objects.count()
        self.assertEqual(blog_posts, 2)

    def test_auto_slug_creation(self):
        pass

    def test_blog_post_dates(self):
        # publication_datetime, creation_datetime, and last_modify_datetime should be checked
        # by default publication_date is creation_date
        pass

    def test_blog_post_likes_dislikes_views_and_reports(self):
        pass

    def test_blog_post_tags(self):
        pass

