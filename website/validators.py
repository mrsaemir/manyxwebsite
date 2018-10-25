from rest_framework.serializers import ValidationError


# validating if a title is unique in the ManyxProject db.
def validate_unique_title(value):
    from .models import ManyxProject
    if ManyxProject.objects.filter(title__iexact=value):
        raise ValidationError('Title should be unique.')