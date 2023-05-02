from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room,Message

# Redirected to login page if user not logged in
@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    #find room based on slug
    room = Room.objects.get(slug=slug)
    # only query the first 25 messages with this room when user first enters
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages':messages})
