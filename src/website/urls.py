from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'admin', views.ManyxProjectAdminViewSet, base_name='admin-project')
router.register(r'', views.ManyxProjectCommonViewSet, base_name='project')
