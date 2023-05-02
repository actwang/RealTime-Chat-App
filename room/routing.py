from django.urls import path,re_path
from . import consumer

websocket_urlpatterns = [
    path('ws/<str:slug>/', consumer.ChatConsumer.as_asgi()),
    #re_path(r"ws/server/", consumer.ChatConsumer.as_asgi())
]