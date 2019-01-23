from rest_framework.routers import DefaultRouter
from .views import ManyxBlogCommonViewSet, ManyxBlogAdminViewSet

router = DefaultRouter()
router.register(r'admin', ManyxBlogAdminViewSet, base_name='admin-blog')
router.register(r'', ManyxBlogCommonViewSet, base_name='blog')
