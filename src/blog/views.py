from rest_framework import viewsets
from .mixins import AnonymousMixin


class ManyxBlogCommonViewSet(AnonymousMixin, viewsets.ReadOnlyModelViewSet):
    queryset = None
    serializer_class = None