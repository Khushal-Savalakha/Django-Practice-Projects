#Topic :-Authentication
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync
import json
from .models import Chat,Group
from channels.db import database_sync_to_async
from django.db.models import ObjectDoesNotExist
from django.utils.timezone import now


# class MySyncConsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         print("Websocket Connected....",event)
        
#         #get default channel layer from a project
#         print("Channel Layer....",self.channel_layer)
#         #get channel Name
#         print("Channel Name....",self.channel_name)
#         #add a channel to a new or existing group
#         self.group_name=self.scope['url_route']['kwargs']['groupkaname']
#         print("Group Name:",self.group_name)
#         async_to_sync(self.channel_layer.group_add)(
#             self.group_name, #group name
#             self.channel_name
#             )
#         self.send({
#             'type':'websocket.accept',
#         })

#    def websocket_receive(self,event):
#         """This code shows username while only sending and receive process"""
#         try:
#             print('Message received from client...',event)
#             print(event['text'])
#             data=json.loads(event['text'])
#             print("Type of Data:",type(data),data)

#             print("--->",self.scope['user'])

#             #Find Group Object
#             group=Group.objects.get(name=self.group_name)
#             if self.scope['user'].is_authenticated:
#                 print("--->Entered in if")
#                 #Create New Chat Object
#                 data['user']=self.scope['user'].username
#                 print("Complete Data:",type(data),data)
#                 chat=Chat(
#                     content=data['msg'],
#                     group=group
#                 )
#                 chat.save()
                
#                 async_to_sync(self.channel_layer.group_send)(self.group_name,{
#                     'type':'chat.message',
#                     'message':json.dumps(data)
#                 })
#             else:
#                 print("--->Entered in else")
#                 # self.send(json.dumps({"msg": "Login Required"}))
#                 self.send({
#                     'type':'websocket.send',
#                     'text':json.dumps({"msg":"Login Required","user":"unknown"})
#                 })
#         except BaseException as error:
#             print(error)
    
#     def chat_message(self,event):
#         print('Event...',event)
#         self.send({
#             'type': 'websocket.send',
#             'text': event['message']
#         })

#     def websocket_disconnect(self,event):
#         print('Websocket Disconnected....',event)
#         #get default channel layer from a project
#         print("Channel Layer....",self.channel_layer)
#         #get channel Name
#         print("Channel Name....",self.channel_name)
#         #add a channel to a new or existing group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.group_name,
#             self.channel_name
#             )
#         raise StopConsumer()



class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected....", event)
        
        # Get default channel layer
        print("Channel Layer....", self.channel_layer)
        print("Channel Name....", self.channel_name)
        
        # Add the channel to a group
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name:", self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.send({
            'type': 'websocket.accept',
        })

    def websocket_receive(self, event):
        try:
            print('Message received from client...', event)
            print(event['text'])
            data = json.loads(event['text'])
            print("Type of Data:", type(data), data)

            print("--->", self.scope['user'])

            # Find Group Object
            group = Group.objects.get(name=self.group_name)
            if self.scope['user'].is_authenticated:
                print("--->Entered in if")
                
                # Add username to the data
                data['user'] = self.scope['user'].username
                print("Complete Data:", type(data), data)

                # Create New Chat Object
                chat = Chat(
                    content=data['msg'],
                    group=group,
                    username=self.scope['user'].username,  # Save username
                    timestamp=now()
                )
                chat.save()

                # Send the updated data to the group
                async_to_sync(self.channel_layer.group_send)(self.group_name, {
                    'type': 'chat.message',
                    'message': json.dumps(data)
                })
            else:
                print("--->Entered in else")
                self.send({
                    'type': 'websocket.send',
                    'text': json.dumps({"msg": "Login Required", "user": "unknown"})
                })
        except BaseException as error:
            print(error)

    def chat_message(self, event):
        print('Event...', event)
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print('Websocket Disconnected....', event)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected....", event)
        
        # Get default channel layer from a project
        print("Channel Layer....", self.channel_layer)
        
        # Get channel Name
        print("Channel Name....", self.channel_name)
        
        # Add a channel to a new or existing group
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name:", self.group_name)
        
        await self.channel_layer.group_add(
            self.group_name,  # Group name
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        try:
            print('Message received from client...', event)
            print(event['text'])
            data=json.loads(event['text'])
            print("Type of Data:",type(data),data)
            #Find Group Object
            group=await database_sync_to_async(Group.objects.get)(name=self.group_name)
            if self.scope['user'].is_authenticated:
                print("--->Entered in if")
                #Create New Chat Object
                chat=Chat(
                    content=data['msg'],
                    group=group
                )
                chat.save()
                data['user']=self.scope['user'].username
                print("Complete Data:",type(data),data)
                async_to_sync(self.channel_layer.group_send)(self.group_name,{
                    'type':'chat.message',
                    'message':event['text']
                })
            else:
                print("--->Entered in else")
                # self.send(json.dumps({"msg": "Login Required"}))
                self.send({
                    'type':'websocket.send',
                    'text':json.dumps({"msg":"Login Required"})
                })
            #Create New Chat Object
            chat=Chat(
                content=data['msg'],
                group=group
            )
            await database_sync_to_async(chat.save)()
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'message': event['text']
                }
            )
        except BaseException as error:
            print(error)

    async def chat_message(self, event):
        print('Event...', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self, event):
        print('Websocket Disconnected....', event)
        
        # Get default channel layer from a project
        print("Channel Layer....", self.channel_layer)
        
        # Get channel Name
        print("Channel Name....", self.channel_name)
        
        # Remove the channel from the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected....", event)

        # Get default channel layer from a project
        print("Channel Layer....", self.channel_layer)

        # Get channel Name
        print("Channel Name....", self.channel_name)

        # Add a channel to a new or existing group
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name:", self.group_name)

        await self.channel_layer.group_add(
            self.group_name,  # Group name
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        try:
            print('Message received from client...', event)
            print(event['text'])
            data = json.loads(event['text'])
            print("Type of Data:", type(data), data)

            # Find Group Object
            group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
            
            if self.scope['user'].is_authenticated:
                print("--->Entered in if")

                # Add username to the data
                data['user'] = self.scope['user'].username
                print("Complete Data:", type(data), data)

                # Create New Chat Object
                chat = Chat(
                    content=data['msg'],
                    group=group,
                    username=self.scope['user'].username,  # Save username
                    timestamp=now()
                )
                await database_sync_to_async(chat.save)()

                # Send the updated data to the group
                await self.channel_layer.group_send(self.group_name, {
                    'type': 'chat.message',
                    'message': json.dumps(data)
                })
            else:
                print("--->Entered in else")
                await self.send({
                    'type': 'websocket.send',
                    'text': json.dumps({"msg": "Login Required", "user": "unknown"})
                })
        except ObjectDoesNotExist:
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({"msg": "Invalid Group", "user": "unknown"})
            })
        except BaseException as error:
            print("Error:", error)

    async def chat_message(self, event):
        print('Event...', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self, event):
        print('Websocket Disconnected....', event)

        # Remove the channel from the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()