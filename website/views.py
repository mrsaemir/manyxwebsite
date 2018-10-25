from rest_framework import viewsets
from .models import ManyxProject
from .serializers import ManyxProjectCommonSerializer


class AnonymousUserMixin:
    paginate_by = 25
    pagination_by_param = 'page_size'
    max_paginate_by = 100


# read only view for demonstration of projects on the main page (unauthorized users)
class ManyxProjectViewSet(AnonymousUserMixin, viewsets.ReadOnlyModelViewSet):
    queryset = ManyxProject.objects.all().order_by('creation_date')
    serializer_class = ManyxProjectCommonSerializer
