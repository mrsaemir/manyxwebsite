from django.urls import re_path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    re_path(r'^api/token/', obtain_auth_token, name='api-token'),
    # re_path(r'^api/', include())
]
