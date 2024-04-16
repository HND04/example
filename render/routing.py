
# routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/pi/', consumers.PiConsumer.as_asgi()),
]
