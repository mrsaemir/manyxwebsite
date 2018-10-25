from rest_framework import serializers, authentication, permissions


class AdminMixin:
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAdminUser,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class AnonymousUserMixin:
    paginate_by = 25
    pagination_by_param = 'page_size'
    max_paginate_by = 100

