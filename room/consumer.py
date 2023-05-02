import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import logging
from .models import Room, Message
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_slug = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = f'chatroom_{self.room_slug}'

        # Add user's channel to group of name room_group_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'Connection successful!',
        }))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        room = text_data_json['room']
        # print(message)
        # print(username)
        # print(room)

        # store the message to DB before broadcasting
        await self.save_message(username, room, message)
        # Broadcast to the channel_layer identified by room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'chat_message',
                'message' : message,
                'username' : username,
                'room' : room
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        print('sending')
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'username': username,
            'room': room
        }))


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    @sync_to_async #this makes it possible for await to store things in the database, Store and wait till it's finished(make others await)
    def save_message(self, username, room, message):
        # diff between get and filter: get will raise error on not found, filter will return empty
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)
        Message.objects.create(user=user, room=room, content=message)
