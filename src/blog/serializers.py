from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework.reverse import reverse
from .models import Blog
from .fields import JDateTimeField
from .validators import validate_tags


class ManyxBlogCommonSerializer(serializers.ModelSerializer):
    auther = serializers.SerializerMethodField()
    publication_datetime = JDateTimeField()

    class Meta:
        model = Blog
        fields = ('title', 'slug', 'auther', 'publication_datetime', 'likes', 'tags', 'text')
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookup_field': 'title'}
        }

    def get_auther(self, obj):
        request = self.context["request"]
        return {
            "auther": obj.auther.username,
            'link': reverse('user-detail', kwargs={'username': obj.auther.username}, request=request)}


class ManyxBlogAdminSerializer(serializers.Serializer):
    created = serializers.SerializerMethodField()
    publication_datetime = JDateTimeField()
    last_modification = serializers.SerializerMethodField()
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField(allow_unicode=True, allow_blank=True,
                                 allow_null=True)
    text = serializers.CharField()
    tags = serializers.JSONField(required=False, validators=[validate_tags])
    reported = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()
    disliked = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()
    auther = serializers.SerializerMethodField()

    @staticmethod
    def get_disliked(obj):
        return obj.dislikes

    @staticmethod
    def get_liked(obj):
        return obj.likes

    @staticmethod
    def get_reported(obj):
        return obj.reports

    @staticmethod
    def get_last_modification(obj):
        return '%s-%s-%s %s:%s' % (obj.last_modified_datetime.year,
                                   obj.last_modified_datetime.month,
                                   obj.last_modified_datetime.day,
                                   obj.last_modified_datetime.hour,
                                   obj.last_modified_datetime.minute)
    @staticmethod
    def get_created(obj):
        return '%s-%s-%s %s:%s' % (obj.creation_datetime.year,
                                   obj.creation_datetime.month,
                                   obj.creation_datetime.day,
                                   obj.creation_datetime.hour,
                                   obj.creation_datetime.minute)

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('admin-blog-detail', kwargs={'slug': obj.slug},
                            request=request),
        }

    def get_auther(self, obj):
        request = self.context["request"]
        return {
            "auther": obj.auther.username,
            'link': reverse('user-detail', kwargs={'username': obj.auther.username}, request=request)}


    @staticmethod
    def get_creation_datetime(obj):
        return obj.creation_datetime

    class Meta:
        model = Blog
        lookup_field = 'title'
        extra_kwargs = {
            'url': {'lookup_field': 'title'}
        }

    def create(self, validated_data):
        instance = Blog()
        # validate title to be unique
        title = validated_data.get('title')
        if not Blog.objects.filter(title__iexact=title):
            instance.title = title
        else:
            raise APIException('title should be unique.')
        slug = validated_data.get('slug')
        if not Blog.objects.filter(slug__iexact=slug):
            instance.slug = slug
        else:
            raise APIException("slug should be unique.")
        instance.publication_datetime = validated_data.get('publication_datetime')
        instance.text = validated_data.get('text')
        instance.tags = validated_data.get('tags')
        instance.auther = self.context['request'].user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        title = validated_data.get('title', '')
        if title:
           if not Blog.objects.filter(title__iexact=title):
               instance.title = title
        slug = validated_data.get('slug')
        if slug:
            if not Blog.objects.filter(slug__iexact=slug):
                instance.slug = slug
        else:
            instance.slug = slug
        instance.publication_datetime = validated_data.get('publication_datetime', instance.publication_datetime)
        instance.text = validated_data.get("text", instance.text)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()
        return instance

