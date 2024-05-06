import time
import logging
from django.http import HttpResponse
from django.core.cache import cache

logger = logging.getLogger(__name__)

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        logger.info(f"Incoming request from IP: {ip_address}")

        request_count_key = f'request_count_{ip_address}'
        block_expiry_key = f'block_expiry_{ip_address}'

        current_time = int(time.time())
        time_window = 10  # Time window in seconds

        # Get the timestamps of the previous requests within the time window
        timestamps = cache.get(request_count_key, [])
        logger.info(f"Previous timestamps: {timestamps}")

        # Remove timestamps older than the time window
        timestamps = [t for t in timestamps if t >= current_time - time_window]
        logger.info(f"Filtered timestamps: {timestamps}")

        # Add the current timestamp to the list
        timestamps.append(current_time)

        # Count the number of requests within the time window
        request_count = len(timestamps)
        logger.info(f"Request count: {request_count}")

        # Set the updated timestamps in the cache
        cache.set(request_count_key, timestamps, timeout=time_window)

        block_expiry = cache.get(block_expiry_key)
        logger.info(f"Block expiry: {block_expiry}")

        if block_expiry and current_time < block_expiry:
            logger.warning(f"IP {ip_address} is blocked. Returning 429 response.")
            return HttpResponse("Too Many Requests. Please try again later.", status=429)

        if request_count > 50:
            logger.warning(f"IP {ip_address} has exceeded the rate limit. Blocking for 30 seconds.")
            cache.set(block_expiry_key, current_time + 30)
            return HttpResponse("Too Many Requests. Please try again after 30 seconds.", status=429)

        logger.info(f"IP {ip_address} is allowed to proceed.")
        response = self.get_response(request)
        return response