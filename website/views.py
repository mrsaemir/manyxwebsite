from rest_framework import viewsets
from .models import ManyxProject
from .serializers import ManyxProjectCommonSerializer, ManyxProjectAdminSerializer
from .mixins import AdminMixin, AnonymousUserMixin


# read only view for demonstration of projects on the main page (unauthorized users)
class ManyxProjectCommonViewSet(AnonymousUserMixin, viewsets.ReadOnlyModelViewSet):
    queryset = ManyxProject.objects.all().order_by('-creation_date')
    serializer_class = ManyxProjectCommonSerializer


class ManyxProjectAdminViewSet(AdminMixin, viewsets.ModelViewSet):
    queryset = ManyxProject.objects.all().order_by('-creation_date')
    serializer_class = ManyxProjectAdminSerializer
