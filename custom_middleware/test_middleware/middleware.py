import requests
import logging
import time

from django.conf import settings

from django.conf import settings
import requests

from django.conf import settings
import requests

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log request details
        logging.info(f"Request: {request.method} {request.path}")

        # Process the request
        response = self.get_response(request)

        # Log response details
        logging.info(f"Response status: {response.status_code}")

        return response

class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        logging.info(f"Request to {request.path} took {duration:.2f} seconds.")
        return response
    
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Custom logic before the view
        logging.info("Executing custom middleware before view.")
        response = self.get_response(request)
        # Custom logic after the view
        logging.info("Executing custom middleware after view.")
        return response