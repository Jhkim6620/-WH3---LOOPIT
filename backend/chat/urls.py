from django.urls import path
from .views import ChatRoomCreateView

urlpatterns = [
    path('room/', ChatRoomCreateView.as_view(), name='chat-room-create'),
]
