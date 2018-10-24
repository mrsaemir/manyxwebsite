from django.contrib.auth.models import AbstractUser
from django.db import models
from .model_validators import validate_mobile_phone_number, social_validator
from django.contrib.postgres.fields import JSONField


# subclassing base user
class ManyxUser(AbstractUser):
    # a place for saving people's social ids
    twitter = models.CharField(max_length=20, validators=[social_validator], blank=True, null=True)
    facebook = models.CharField(max_length=20, validators=[social_validator], blank=True, null=True)
    instagram = models.CharField(max_length=20, validators=[social_validator], blank=True, null=True)
    website = models.CharField(max_length=20, validators=[social_validator], blank=True, null=True)
    telegram = models.CharField(max_length=20, validators=[social_validator], blank=True, null=True)
    # example for mobile phone number would be : 09122345678 (11 digits starting with 09)
    mobile_phone = models.CharField(max_length=11, validators=[validate_mobile_phone_number], blank=True, null=True)
    # description of one's life and work:
    description = models.TextField(blank=True, null=True)
    # title for each person
    title = models.CharField(max_length=40)
    # we use tags to connect each user to related subjects. that is why we have user tags.
    # each user can have multiple custom tags or nothing at all.
    tags = JSONField(null=True)

    # introducing a user
    def __str__(self):
        return self.first_name + self.last_name or self.last_name or self.username

    # mobile phone number is not included in get_social_info func.
    def get_social_info(self):
        info = {}
        if self.first_name and self.last_name:
            info["full_name"] = self.first_name + self.last_name
        elif self.last_name:
            info["full_name"] = self.last_name
        else:
            info["full_name"] = self.username
        if self.twitter:
            info["twitter"] = 'https://twitter.com/' + self.twitter
        if self.facebook:
            info["facebook"] = 'http://www.facebook.com/' + self.facebook
        if self.website:
            info["website"] = self.website
        if self.telegram:
            info['telegram'] = 'https://telegram.me/' + self.telegram
        if self.instagram:
            info['instagram']= 'https://www.instagram.com/' + self.instagram
        # returning a dictionary of one's social info and identity
        return info
