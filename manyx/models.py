import json
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import JSONField
from rest_framework.reverse import reverse


# subclassing base user
class ManyxUser(AbstractUser):
    # a place for saving people's social ids
    social = JSONField(null=True)
    # example for mobile phone number would be : 09122345678 (11 digits starting with 09)
    mobile_phone = models.CharField(max_length=11, blank=True, null=True)
    # description of one's life and work:
    description = models.TextField(blank=True, null=True)
    # title for each person
    title = models.CharField(max_length=40, blank=True, null=True)
    # we use tags to connect each user to related subjects. that is why we have user tags.
    # each user can have multiple custom tags or nothing at all.
    tags = JSONField(null=True)

    # introducing a user
    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.last_name:
            return self.last_name
        else:
            return self.username

    # mobile phone number is not included in get_social_info func.
    def get_social_info(self, request):
        info = {}
        # setting user's name
        info["full_name"] = self.__str__()
        # setting user's social info
        if self.social:
            social_info = json.loads(self.social)
            for k, v in social_info.items():
                info[str(k)] = '/%s/' % self.username + str(k)
                info[str(k)] = reverse('social_refer_counter', kwargs={'username': self.username, 'social_service': str(k)},
                                       request=request)
        return info

    # returns the date in which the user is registered.
    def since(self):
        from jalali_date import date2jalali
        return date2jalali(self.date_joined).strftime('13%y-%m-%d')


# counting refers to a person's social accounts
class SocialReferCounter(models.Model):
    # counter for social media
    counts = models.PositiveIntegerField(default=0)
    # name for social media service
    account = models.CharField(max_length=200)
    account_id = models.CharField(max_length=200)
    user = models.ForeignKey(ManyxUser, on_delete=models.SET_NULL, null=True)

    # adding to a record or creating a new one.
    def add_record(self, user, account, account_id):
        refer = SocialReferCounter.objects.filter(
            account=account,
            account_id=account_id,
            user=user
        )
        # if requested resource exists:
        if refer:
            refer = refer[0]
            # this means that the resource is requested
            # and this request should be counted
            refer.counts = refer.counts + 1
            refer.save()
        else:
            # creating a new refer because it does not exist
            refer = SocialReferCounter()
            refer.account = account
            refer.account_id = account_id
            refer.user = user
            refer.counts = 1
            refer.save()
