from rest_framework import viewsets
from .mixins import AnonymousMixin, AdminMixin
from .models import Blog
from .serializers import ManyxBlogCommonSerializer, ManyxBlogAdminSerializer


class ManyxBlogCommonViewSet(AnonymousMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Blog.published.all().order_by("-publication_datetime")
    serializer_class = ManyxBlogCommonSerializer


class ManyxBlogAdminViewSet(AdminMixin, viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by("-publication_datetime")
    serializer_class = ManyxBlogAdminSerializer
    lookup_field = 'slug'
