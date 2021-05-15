from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room

from django.http import HttpResponse

@login_required
def profile(request, active):
    
    rooms = Room.objects.order_by("title")
       
    try:
        if int(active) in Room.objects.values_list('id', flat=True):
            chat = Room.objects.get(id=active)
            return render(request, "index.html", {
                "rooms": rooms, "active": active, "chat": chat
            })
            
        else:
            return render(request, "404.html")
    except ValueError:
        return render(request, "404.html")
    

@login_required
def index(request):
    rooms = Room.objects.order_by("title")

    return render(request, "home.html", {
        "rooms": rooms, 
    })



