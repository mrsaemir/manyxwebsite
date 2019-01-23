from rest_framework import viewsets
from .mixins import AnonymousMixin, AdminMixin
from .models import Blog
from .serializers import ManyxBlogCommonSerializer


class ManyxBlogCommonViewSet(AnonymousMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Blog.published.all()
    serializer_class = ManyxBlogCommonSerializer


class ManyxBlogAdminViewSet(AdminMixin, viewsets.ModelViewSet):
    queryset = None
    serializer_class = None

