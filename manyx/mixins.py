from rest_framework import authentication
from rest_framework import permissions


class AnonymousUserMixin:
    paginate_by = 25
    pagination_by_param = 'page_size'
    max_paginate_by = 100


class AdminMixin:
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAdminUser,
    )
