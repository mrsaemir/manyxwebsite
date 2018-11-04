from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import ManyxUser


class ManyxUserCommonSerializer(serializers.ModelSerializer):
    social_info = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

    class Meta:
        model = ManyxUser
        fields = ('title', 'description', 'tags', 'social_info', 'links')
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def get_social_info(self, obj):
        request = self.context['request']
        return obj.get_social_info(request)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('user-detail', kwargs={'username': obj.username}, request=request)
        }
