from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room

from django.http import HttpResponse

@login_required
def profile(request, active):
    
    rooms = Room.objects.order_by("title")
    
    try:
        if int(active) in Room.objects.values_list('id', flat=True):
            # Render that in the index template
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
    
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "home.html", {
        "rooms": rooms, 
    })



