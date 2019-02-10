from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from ipware import get_client_ip
from django.http import HttpResponse


# website will be deactivated while it is in maintenance mode.
# note : in order for this middleware to work it is needed that
# a reverse proxy(like nginx) sets the appropriate header.(HTTP_X_REAL_IP)
class MaintenanceMode(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        if settings.MAINTENANCE:
            # ip, is_routable = get_client_ip(request)
            ip = request.META.get("X-Forwarded-For", None)
            raise IOError(ip)
            if ip is not None:
                if ip not in settings.DEBUG_IPS:
                    return HttpResponse('Under Maintenance! Try Again Later ...', status=503)
            else:
                return HttpResponse('Under Maintenance! Try Again Later ...', status=503)
