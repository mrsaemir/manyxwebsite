from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from ipware import get_client_ip
from django.http import HttpResponse


# website will be deactivated while it is in maintenance mode.
class MaintenanceMode(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        ip, is_routable = get_client_ip(request)

        # if debug is ON, maintenance mode will be ignored.
        if settings.DEBUG:
            return None

        if settings.MAINTENANCE:
            if ip is not None:
                # if request is from a maintainer, let them see the site
                # with DEBUG=True
                if ip in settings.DEBUG_IPS:
                    settings.DEBUG = True
                    return None
            # if request is from a none maintainer ip, then show them
            # the maintenance page.
            settings.DEBUG = False
            return HttpResponse('Under Maintenance! Try Again Later ...', status=503)



