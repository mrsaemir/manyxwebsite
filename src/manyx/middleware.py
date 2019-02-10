from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from ipware import get_client_ip
from django.http import HttpResponse


# website will be deactivated while it is in maintenance mode.
class MaintenanceMode(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        pass
