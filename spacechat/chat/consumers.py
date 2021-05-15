from django.conf import settings

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Room
from .utils import get_room_or_error, message_db
import datetime
import time

# http://channels.readthedocs.io/en/latest/topics/consumers.html
class ChatConsumer(AsyncJsonWebsocketConsumer):

    ##### WebSocket event handlers                  
    async def connect(self):
        
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            await self.accept()
        self.rooms = set()

    async def receive_json(self, content):
              
        command = content.get("command", None)
        print(content)
        try:
            if command == "join":
                await self.join_room(content["room"])
            elif command == "leave":
                await self.leave_room(content["room"])
            elif command == "send":
                await self.send_room(content["room"], content["message"])            
        except:
            await self.send_json({"error": "Error command :c"})

    async def disconnect(self, code):
       
        for room_id in list(self.rooms):
            try:
                await self.leave_room(room_id)
            except:
                print("Error on disconnect!!!")

    async def join_room(self, room_id):
       
        room = await get_room_or_error(room_id, self.scope["user"])
        
        self.rooms.add(room_id)
        await self.channel_layer.group_add(
            room.group_name,
            self.channel_name,
        )
        #await self.send_json({
        #    "join": str(room.id),
        #    "title": room.title,
        #})

    async def leave_room(self, room_id):
       
        room = await get_room_or_error(room_id, self.scope["user"])       
        self.rooms.discard(room_id)
        await self.channel_layer.group_discard(
            room.group_name,
            self.channel_name,
        )
        #await self.send_json({
        #    "leave": str(room.id),
        #})

    async def send_room(self, room_id, message):
        
        if message.isspace() or message == '':
            print("Drop message.")
        else:     
            if room_id not in self.rooms:
                await self.send_json({"error": "You are not joined in this room."})

            if message != "":
                room = await get_room_or_error(room_id, self.scope["user"])
                await self.channel_layer.group_send(
                    room.group_name,
                    {
                        "type": "chat.message",
                        "room_id": room_id,
                        "username": self.scope["user"].username,
                        "message": message,
                    }
                )
                     
    async def chat_join(self, event):
        """
        Do something when someone join left chat.
        """
           
    async def chat_leave(self, event):
        """
        Do something when someone left chat.
        """
    
    async def chat_message(self, event):
     
        time_now = str(time.strftime("%c"))
        await self.send_json(
            {
                "msg_type": settings.MSG_TYPE_MESSAGE,
                "room": event["room_id"],
                "username": event["username"],
                "message": event["message"],
                "timestamp": time_now
            },
        )
        await message_db(int(event["room_id"]), event["username"], event["message"], time_now, settings.MSG_TYPE_MESSAGE)
        
        
