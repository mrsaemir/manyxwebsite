from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import ManyxProject
from .fields import JDateField
from .validators import validate_unique_slug, validate_unique_title


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


# ManyxProject Serializer for admin
class ManyxProjectAdminSerializer(serializers.Serializer):
    slug = serializers.SlugField(allow_unicode=True, allow_blank=True,
                                 allow_null=True)
    title = serializers.CharField(max_length=30)
    snapshot = serializers.ImageField(allow_null=True)
    start_date = JDateField()
    # implemented allow_null in fields from scratch!
    end_date = JDateField(allow_null=True)
    live_url = serializers.URLField(allow_null=True)
    git_repository_url = serializers.URLField(allow_null=True)
    estimated_hours = serializers.IntegerField(allow_null=True)
    team_members = serializers.JSONField(allow_null=True)
    links = serializers.SerializerMethodField()

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('admin-project-detail', kwargs={'slug': obj.slug},
                            request=request),
        }

    def create(self, validated_data):
        # creating the new instance
        validate_unique_title(value=validated_data.get('title'))
        instance = ManyxProject(**validated_data)
        # validating unique slug should occur after slug initialization in models
        validate_unique_slug(value=instance.slug)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # validating slug uniqueness
        validate_unique_slug(value=validated_data.get('slug'), instance=instance)
        instance.slug = validated_data.get('slug', instance.slug)
        # validating title uniqueness
        validate_unique_title(value=validated_data.get('title'), instance=instance)
        instance.title = validated_data.get('title', instance.title)
        instance.snapshot = validated_data.get('snapshot', instance.snapshot)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.live_url = validated_data.get('live_url', instance.live_url)
        instance.git_repository_url = validated_data.get('git_repository_url', instance.git_repository_url)
        instance.estimated_hours = validated_data.get('estimated_hours', instance.estimated_hours)
        instance.team_members = validated_data.get('team_members', instance.team_members)
        instance.save()
        return instance
