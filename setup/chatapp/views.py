import re
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'chatapp/index.html',{})


def chat(request, room_name):
    return render(request, 'chatapp/chat.html', {'roomname': room_name})