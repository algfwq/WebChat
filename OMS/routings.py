from django.urls import path
from app.consumers import ChatConsumer

websocket_urlpatterns = [
    path('room/',ChatConsumer.as_asgi()),
]