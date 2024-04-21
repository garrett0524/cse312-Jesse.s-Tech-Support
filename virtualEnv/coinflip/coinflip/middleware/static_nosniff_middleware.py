from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class StaticNoSniffMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith(settings.STATIC_URL):
            response['X-Content-Type-Options'] = 'nosniff'
        return response