from django.urls import re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from website.urls import router as website_router


urlpatterns = [
    re_path(r'^api/token/', obtain_auth_token, name='api-token'),
    re_path(r'^', include(website_router.urls)),
]
