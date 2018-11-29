from django.urls import re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from website.urls import router as website_router
from .views import ManyxUserViewSet, social_refer_counter, ManyxUserAdminViewSet
from blog.urls import router as blog_router

# setting router for manyx user views
manyx_router = DefaultRouter()
manyx_router.register(r'admin', ManyxUserAdminViewSet, base_name='admin-user')
manyx_router.register(r'', ManyxUserViewSet, base_name='user')


# manyxwebsite url patterns
manyx_url_patterns = [
    re_path(r'^manyx/', include(manyx_router.urls)),
    re_path(r'^manyx/social/(?P<username>[_\w]+)/(?P<social_service>[_\w]+)',
            social_refer_counter, name='social_refer_counter')
]

#manyxblog url patterns
manyxblog_url_patterns = [
    re_path(r'^blog/', include(blog_router.urls)),
]


project_url_patterns = [
    re_path(r'^project/', include(website_router.urls)),
]

urlpatterns = manyx_url_patterns + project_url_patterns + manyxblog_url_patterns + [
    # token url
    re_path(r'^api/token/', obtain_auth_token, name='api-token'),
]

