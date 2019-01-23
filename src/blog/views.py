from rest_framework import viewsets
from .mixins import AnonymousMixin
from .models import Blog
from .serializers import ManyxBlogCommonSerializer


class ManyxBlogCommonViewSet(AnonymousMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Blog.published.all()
    serializer_class = ManyxBlogCommonSerializer
