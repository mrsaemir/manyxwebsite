from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'project', views.ManyxProjectCommonViewSet, base_name='project')
router.register(r'admin/project', views.ManyxProjectAdminViewSet, base_name='admin-project')