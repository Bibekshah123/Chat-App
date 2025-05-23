from django.shortcuts import render
from .models import Room,Message
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import   UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

def rooms(request):
    rooms=Room.objects.all()
    return render(request, "home.html",{"rooms":rooms})

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})



# class RoomListView(ListView):
#     model = Room
#     template_name = "rooms.html"
#     context_object_name = "rooms"

# class RoomDetailView(DetailView):
#     model = Room
#     template_name = "room.html"
#     context_object_name = "room"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         room = self.get_object()
#         context['room_name'] = room.name
#         context['slug'] = room.slug
#         context['messages'] = Message.objects.filter(room=room)
        # return context