from rest_framework import authentication, permissions


class AdminMixin:
    authentication_classes = (
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAdminUser,
    )


class AnonymousUserMixin:
    paginate_by = 25
    pagination_by_param = 'page_size'
    max_paginate_by = 100

