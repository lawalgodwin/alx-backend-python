from django.conf import settings
from datetime import datetime

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