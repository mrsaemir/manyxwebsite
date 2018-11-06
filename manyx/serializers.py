from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework.exceptions import APIException
from .models import ManyxUser
from .validators import validate_mobile_phone_number, validate_username, validate_tags, validate_social


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


class ManyxUserAdminSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, validators=[validate_username])
    password_input = serializers.CharField(min_length=8, max_length=150, required=False)
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    social = serializers.JSONField(required=False, validators=[validate_social])
    mobile_phone = serializers.CharField(required=False, validators=[validate_mobile_phone_number])
    description = serializers.CharField(required=False)
    title = serializers.CharField(max_length=40, required=False)
    since = serializers.SerializerMethodField()
    tags = serializers.JSONField(required=False, validators=[validate_tags])
    links = serializers.SerializerMethodField()

    class Meta:
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('admin-user-detail', kwargs={'username': obj.username}, request=request)
        }

    @staticmethod
    def get_since(obj):
        return obj.since()

    def create(self, validated_data):
        instance = ManyxUser()
        # validate username is unique:
        username = validated_data.get('username')
        if not ManyxUser.objects.filter(username=username).exclude(pk=instance.pk):
            instance.username = username
        else:
            raise APIException('Username Exists!Try Another.')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.email = validated_data.get('email')
        instance.social = validated_data.get('social')
        instance.mobile_phone = validated_data.get('mobile_phone')
        instance.description = validated_data.get('description')
        instance.title = validated_data.get('title')
        instance.tags = validated_data.get('tags')
        instance.save()
        # setting password
        # if password is empty through the process of sign up then raise an error
        password = validated_data.get('password_input')
        if not password:
            raise APIException("Password is Required.")
        instance.set_password(password)
        return instance

    def update(self, instance, validated_data):
        username = validated_data.get('username')
        if not ManyxUser.objects.filter(username=username).exclude(pk=instance.pk):
            instance.username = username
        else:
            raise APIException('Username Exists!Try Another.')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.social = validated_data.get('social', instance.social)
        instance.mobile_phone = validated_data.get('mobile_phone', instance.mobile_phone)
        instance.description = validated_data.get('description', instance.description)
        instance.title = validated_data.get('title', instance.title)
        instance.tags = validated_data.get('tags', instance.tags)
        # getting password
        password = validated_data.get('password_input')
        # if a password is not provided then just ignore it and don't change the password.
        if password:
            instance.set_password(password)
        instance.save()
        return instance
