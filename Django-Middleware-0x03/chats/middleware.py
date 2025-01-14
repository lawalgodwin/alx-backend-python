from django.conf import settings
from datetime import datetime
from django.http.response import HttpResponseForbidden

class RequestLoggingMiddleware:
    """A middleware that logs each user’s requests to a file, 
    including the timestamp, user and the request path
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # manipulate the request object before it reaches the view
        log_file = f"{settings.REQUESTS_LOG_FILE}"
        with open(log_file, "a") as log_file:
            log_message = f"{datetime.now()} - User: {request.user} - Path: {request.path}\n"
            log_file.write(log_message)
        response = self.get_response(request)
        # manipulate the response object before it reaches the client
        return response


class RestrictAccessByTimeMiddleware:
    """A middleware that restricts access to the
    messaging app during certain hours of the day
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        server_current_hour = datetime.now().hour
        if (server_current_hour < 9) or (server_current_hour >= 18):
            # access denied for access outside 9am - 6pm
            return HttpResponseForbidden("Access denied....Try again between 9am-6pm")
        response = self.get_response(request)
        return response