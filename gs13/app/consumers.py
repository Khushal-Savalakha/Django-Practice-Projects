# Topic - Generic Consumer -JsonWebsocketConsumer and AsyncJsonWebsocketConsumer

from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):

    def connect(self):
        """This handler is called when client initially opens a connection
        and is about to finish the websocket handshake"""
        print("Websocket Connected...")
        self.accept()
    
    def receive_json(self,content,**kwargs):
        """This handler is called when data received from client 
        with decoded JSON content"""
        print("Message received from client...",content['msg'])
        print("type of Message received from client...",type(content))
        self.send_json({'message':'Message from server to client'})
    
    def disconnect(self,close_code):
        print("Websocket Connected...",close_code)

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        """This handler is called when client initially opens a connection
        and is about to finish the websocket handshake"""
        print("Websocket Connected...")
        await self.accept()
    
    async def receive_json(self,content,**kwargs):
        """This handler is called when data received from client 
        with decoded JSON content"""
        print("Message received from client...",content['msg'])
        print("type of Message received from client...",type(content))
        await self.send_json({'message':'Message from server to client'})
    
    async def disconnect(self,close_code):
        print("Websocket Connected...",close_code)