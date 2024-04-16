
# routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('wss/pi/', consumers.PiConsumer.as_asgi()),
]
