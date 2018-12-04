from rest_framework.routers import DefaultRouter
from .views import ManyxBlogCommonViewSet

router = DefaultRouter()
router.register(r'', ManyxBlogCommonViewSet, base_name='blog')
