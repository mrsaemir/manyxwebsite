from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from ipware import get_client_ip
from django.http import HttpResponse


# website will be deactivated while it is in maintenance mode.
class MaintenanceMode(MiddlewareMixin):
    def process_request(self, request):
        ip, is_routable = get_client_ip(request)

        if settings.MAINTENANCE:
            if ip is not None:
                if ip not in settings.DEBUG_IPS:
                    return HttpResponse('Under Maintenance! Try Again Later ...', status=503)
            else:
                return HttpResponse('Under Maintenance! Try Again Later ...', status=503)
