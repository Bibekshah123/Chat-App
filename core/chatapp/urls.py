from django.urls import path

from . import views
from .views import *


urlpatterns = [
    # path("", RoomListView.as_view(), name='rooms'),
    # path('room/<slug:slug>/', RoomDetailView.as_view(), name='room'),
    path("", views.rooms, name="rooms"),
    path("<str:slug>", views.room, name="room"),
    
    path("register/", SignUpView.as_view(), name="register"),

]