from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.postgres.fields import JSONField
from rest_framework.exceptions import APIException
import jdatetime


# a model for saving details about our projects.
class ManyxProject(models.Model):
    creation_date = jmodels.jDateTimeField(auto_now_add=True)
    # info about project.
    slug = models.SlugField(allow_unicode=True, unique=True, db_index=True)
    title = models.CharField(max_length=30, unique=True)
    snapshot = models.ImageField(upload_to="snapshots", null=True)
    start_date = jmodels.jDateField()
    end_date = jmodels.jDateField(null=True)
    live_url = models.URLField(blank=True, null=True)
    git_repository_url = models.URLField(blank=True, null=True)
    # work hours on each project
    estimated_hours = models.PositiveIntegerField(null=True)
    # info about creators.
    team_members = JSONField(null=True, blank=True)

    def __str__(self):
        return '%s (Ended: %s)' % (self.title, self.end_date or False)

    # returns a boolean if a project is under development.
    @property
    def under_development(self):
        if self.end_date:
            return False
        return True

    def get_slug(self):
        from django.utils.text import slugify
        return slugify(self.title, allow_unicode=True) or self.title

    # do a sanity check to ensure that a finished project has an end date and vice versa.
    def validate_fields(self):
        if self.end_date:
            if self.end_date <= self.start_date:
                raise APIException("End time can't be before start time")
        if self.start_date >= jdatetime.date.today():
            if self.end_date:
                raise APIException("Future projects can't be finished")

    # saving an instance
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        # validate related fields before performing save action
        self.validate_fields()
        # automatically setting slug if nothing is provided.
        if not self.slug:
            self.slug = self.get_slug()
        return super(ManyxProject, self).save(*args, **kwargs)

