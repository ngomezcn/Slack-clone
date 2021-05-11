from .models import Room
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async

import json
# https://stackoverflow.com/questions/48358162/how-to-append-delete-data-from-jsonfield-in-django
# https://stackoverflow.com/questions/61926359/django-synchronousonlyoperation-you-cannot-call-this-from-an-async-context-u

@database_sync_to_async
def test(room_id, username, message, time, msg_type):
   
    obj = Room.objects.get(id=room_id)
   
    index = "msg" + str(obj.counter)
    obj.my_json[index] = {}    
    a_dictionary =  {index: {"msg_type": msg_type, "room": room_id, "username": username, "message": message, "timestamp": time }}
    #b_dictionary = {"info": {"nmsg": obj.counter}}
    
   # obj.my_json.update(b_dictionary)
    obj.my_json.update(a_dictionary)
        
    #print(json.dumps(json.loads(json.dumps(obj.my_json)) , indent=4, sort_keys=True))
    obj.counter+= 1
    obj.save()
    return 'HOLA'

'''
{
	"01": {
		"msg_type": "Click Here",
		"username": "bold",
		"message": "text1",
		"timestamp": "250"
	}
}
'''

