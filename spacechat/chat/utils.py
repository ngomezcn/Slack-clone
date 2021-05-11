from channels.db import database_sync_to_async

from .exceptions import ClientError
from .models import Room
from asgiref.sync import sync_to_async

import json
# https://stackoverflow.com/questions/48358162/how-to-append-delete-data-from-jsonfield-in-django
# https://stackoverflow.com/questions/61926359/django-synchronousonlyoperation-you-cannot-call-this-from-an-async-context-u


# This decorator turns this function from a synchronous function into an async one
# we can call from our async consumers, that handles Django DBs correctly.
# For more, see http://channels.readthedocs.io/en/latest/topics/databases.html
@database_sync_to_async
def get_room_or_error(room_id, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Check if the user is logged in
    if not user.is_authenticated:
        raise ClientError("USER_HAS_TO_LOGIN")
    # Find the room they requested (by ID)
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise ClientError("ROOM_INVALID")
    return room


@database_sync_to_async
def message_db(room_id, username, message, time, msg_type):
   
    obj = Room.objects.get(id=room_id)
   
    index = "msg" + str(obj.counter)
    obj.my_json[index] = {}    
    a_dictionary =  {index: {"msg_type": msg_type, "room": room_id, "username": username, "message": message, "timestamp": time }}
    
    obj.my_json.update(a_dictionary)
        
    obj.counter+= 1
    obj.save()



