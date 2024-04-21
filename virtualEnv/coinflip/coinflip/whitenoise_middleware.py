# whitenoise_middleware.py
from whitenoise import WhiteNoise
import os

class WhiteNoiseMiddleware:
    def __init__(self, application):
        self.application = WhiteNoise(application, root=os.path.join(os.getcwd(), 'staticfiles'))

    async def __call__(self, scope, receive, send):
        return await self.application(scope, receive, send)