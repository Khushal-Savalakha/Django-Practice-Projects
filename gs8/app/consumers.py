#Topic :-Chat App with Static Group Name
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Websocket Connected....",event)
        
        #get default channel layer from a project
        print("Channel Layer....",self.channel_layer)
        #get channel Name
        print("Channel Name....",self.channel_name)
        #add a channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)(
            'Friends', #group name
            self.channel_name
            )
        self.send({
            'type':'websocket.accept',
        })

    def websocket_receive(self,event):
        try:
            print('Message received from client...',event)
            print(event['text'])
            async_to_sync(self.channel_layer.group_send)('Friends',{
                'type':'chat.message',
                'message':event['text']
            })
        except BaseException as error:
            print(error)
    
    def chat_message(self,event):
        print('Event...',event)
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self,event):
        print('Websocket Disconnected....',event)
        #get default channel layer from a project
        print("Channel Layer....",self.channel_layer)
        #get channel Name
        print("Channel Name....",self.channel_name)
        #add a channel to a new or existing group
        async_to_sync(self.channel_layer.group_discard)(
            'programmers',
            self.channel_name
            )
        raise StopConsumer()



class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected....", event)
        
        # Get default channel layer from the project
        print("Channel Layer....", self.channel_layer)
        # Get channel name
        print("Channel Name....", self.channel_name)
        
        # Add a channel to a new or existing group
        await self.channel_layer.group_add(
            'Friends',  # Group name
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_receive(self, event):
        try:
            print('Message received from client...', event)
            print(event['text'])
            await self.channel_layer.group_send(
                'Friends',  # Group name
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
        # Get default channel layer from the project
        print("Channel Layer....", self.channel_layer)
        # Get channel name
        print("Channel Name....", self.channel_name)
        
        # Remove a channel from the group
        await self.channel_layer.group_discard(
            'Friends',  # Group name
            self.channel_name
        )
        raise StopConsumer()
