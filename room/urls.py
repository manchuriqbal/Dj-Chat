from django.urls import path, include
from . import views

from room.routing import websocket_urlpatterns

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>', views.room, name='room'),
    path('ws/', include(websocket_urlpatterns)),

]