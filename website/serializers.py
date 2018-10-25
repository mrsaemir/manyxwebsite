from rest_framework import serializers
from .models import ManyxProject


# serializer for demonstration on main page
# this serializer is readonly.
class ManyxProjectCommonSerializer(serializers.ModelSerializer):

    class Meta:
        model = ManyxProject
        # only insensitive info is available through the serializer
        fields = ('title', 'start_date', 'end_date', 'live_url')
