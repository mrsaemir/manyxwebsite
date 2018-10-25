from rest_framework import serializers
from .models import ManyxProject


# serializer for demonstration on main page
# this serializer is readonly.
class ManyxProjectCommonSerializer(serializers.ModelSerializer):
    under_development = serializers.SerializerMethodField()

    class Meta:
        model = ManyxProject
        # only insensitive info is available through the serializer
        fields = ('title', 'snapshot', 'start_date', 'end_date', 'live_url', 'under_development')

    @staticmethod
    def get_under_development(obj):
        return obj.under_development