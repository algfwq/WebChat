from django.urls import path
from app.consumers import login

websocket_urlpatterns = [
    path('login_ws/', login.as_asgi()),
]