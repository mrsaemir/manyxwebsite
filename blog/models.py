from django.db import models
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
ManyxUser = get_user_model()


# Create your models here.
class Blog(models.Model):
    creation_datetime = jmodels.jDateTimeField(auto_now_add=True)
    last_modified_datetime = jmodels.jDateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, db_index=True)
    # because it's blog post title, a maximum length of 100 is ideal.
    title = models.CharField(max_length=100)
    text = models.TextField()
    auther = models.ForeignKey(ManyxUser, on_delete=models.SET_NULL, null=True)

    def get_slug(self):
        from django.utils.text import slugify
        return slugify(self.title, allow_unicode=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()
        return super(Blog, self).save(*args, **kwargs)