from django.urls import re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from website.urls import router as website_router
from .views import ManyxUserViewSet, social_refer_counter

# setting router for manyx user views
manyx_router = DefaultRouter()
manyx_router.register(r'', ManyxUserViewSet, base_name='user')


# manyxwebsite url patterns
manyx_url_patterns = [
    re_path(r'^manyx/', include(manyx_router.urls)),
    re_path(r'^manyx/(?P<username>[_\w]+)/(?P<social_service>[_\w]+)', social_refer_counter, name='social_refer_counter')
]


project_url_patterns = [
    re_path(r'^project/', include(website_router.urls)),
]

urlpatterns = manyx_url_patterns + project_url_patterns + [
    # token url
    re_path(r'^api/token/', obtain_auth_token, name='api-token'),
]