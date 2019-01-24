from rest_framework import authentication, permissions


class AnonymousMixin:
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
