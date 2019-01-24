from rest_framework.exceptions import APIException


# validating if a title is unique in the ManyxProject db.
def validate_unique_title(value, instance=None):
    from .models import ManyxProject
    if not instance:
        if ManyxProject.objects.filter(title__iexact=value):
            raise APIException('Title should be unique.')
    else:
        if ManyxProject.objects.filter(title__iexact=value).exclude(pk=instance.pk):
            raise APIException('Title should be unique.')


# validating slug to be unique
def validate_unique_slug(value, instance=None):
    from .models import ManyxProject
    if not instance:
        if ManyxProject.objects.filter(slug__iexact=value):
            raise APIException('Slug is not set or should be unique.')
    else:
        if ManyxProject.objects.filter(slug__iexact=value).exclude(pk=instance.pk):
            raise APIException('Slug is not set or should be unique.')
