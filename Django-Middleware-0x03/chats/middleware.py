from collections import defaultdict
import time
from django.conf import settings
from datetime import datetime
from django.http import JsonResponse
from django.http.response import HttpResponseForbidden
from http import HTTPMethod

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


class OffensiveLanguageMiddleware:
    """A middleware that limits the number of chat messages a user can send
    within a certain time window, based on their IP address.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # This dictionary will store message timestamps for each IP
        self.ip_message_log = defaultdict(list)

    def __call__(self, request):
        # Process the request if it's a POST request for chat messages
        if request.method == HTTPMethod.POST:
            ip_address = self.get_client_ip(request)
            current_time = time.time()

            # Clean up old timestamps (remove timestamps older than 1 minute)
            self.ip_message_log[ip_address] = [
                timestamp for timestamp in self.ip_message_log[ip_address] 
                if current_time - timestamp < 60
            ]
            
            # Check if the number of messages exceeds the limit
            if len(self.ip_message_log[ip_address]) >= 5:
                return JsonResponse(
                    {"error": "Message limit exceeded. Please try again later."},
                    status=429
                )

            # Add the current timestamp to the list for this IP
            self.ip_message_log[ip_address].append(current_time)

        # Continue processing the request
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """
        Helper function to extract the IP address from the request.
        This might need adjustment depending on your deployment.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        return ip_address


class RolepermissionMiddleware:
    """A middleware that checks the user’s role i.e admin, before
    allowing access to specific actions
    """
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        allowed_roles = ["admin", "moderator"]
        user = request.user
        user_role = "guest"
        if hasattr(user, "role"):
            user_role = user.role
        if user_role not in allowed_roles:
            return HttpResponseForbidden("You do not have the permission to perform this action")
        response = self.get_response(request)
        return response
