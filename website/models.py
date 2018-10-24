from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
import jdatetime


# a model for saving details about our projects.
class ManyxProject(models.Model):
    # info about project.
    title = models.CharField(max_length=40)
    snapshot = models.ImageField(upload_to="snapshots")
    start_date = jmodels.jDateField()
    end_date = jmodels.jDateField(null=True)
    live_url = models.URLField(blank=True)
    git_repository_url = models.URLField(blank=True)
    # work hours on each project
    estimated_hours = models.PositiveIntegerField(null=True)
    # info about creators.
    team_members = JSONField(null=True, blank=True)

    def __str__(self):
        return '%s (Ended: %s)' % (self.title, self.end_date) or self.title

    # returns a boolean if a project is under development.
    @property
    def under_development(self):
        if self.end_date:
            return False
        return True

    # do a sanity check to ensure that a finished project has an end date and vice versa.
    def validate_fields(self):
        if self.end_date:
            if self.end_date <= self.start_date:
                raise ValidationError('زمان پایان نمیتواند زودتر یا برابر با زمان آغاز باشد.')
        if self.start_date >= jdatetime.date.today():
            if self.end_date:
                raise ValidationError('پروژه های آینده نمیتوانند تمام شده باشند.')

    # saving an instance
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        # validate related fields before performing save action
        self.validate_fields()
        return super(ManyxProject, self).save(*args, **kwargs)

