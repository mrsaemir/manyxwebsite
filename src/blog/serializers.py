from rest_framework import serializers
from .models import Blog


class ManyxBlogCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'slug', 'auther', 'publication_datetime', 'likes', 'tags', 'text')
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookup_field': 'title'}
        }
