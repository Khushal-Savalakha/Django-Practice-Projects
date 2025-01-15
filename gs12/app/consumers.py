# Topic - Generic Consumer -WebsocketConsumer and AsyncWebsocketConsumer
#Real-time Data Example
#Real-time Data Example With Front End

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        """This handler is called when client initially opens
        a connection and is about to finish the WebSocket handshake."""
        print('Websocket Connected...')
        self.accept()
    
    def receive(self, text_data=None, bytes_data=None):
        """Handler is called when data received from client"""
        print('Message Received from Client...', text_data)
        
        if text_data == "close":
            self.send(text_data="=>Connection close using self.close()")
            self.close(code=3333)  # Close connection before sending any further messages
            return  # Ensure no more messages are sent after closing
        for i in range(50):
            self.send(text_data=str(i))
            sleep(1)
        # self.send(bytes_data=data)  # To send Binary data
        # self.send(text_data="Message from server to Client")  # Send data to client

    def disconnect(self, close_code):
        """This handler is called when either connection to the client
        is lost, either from the client closing the connection, the server
        closing the connection, or loss of the socket."""
        print('Websocket Disconnected...', close_code)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """This handler is called when client initially opens
        a connection and is about to finish the WebSocket handshake."""
        print('Websocket Connected...')
        await self.accept()
    
    async def receive(self, text_data=None, bytes_data=None):
        """Handler is called when data received from client"""
        print('Message Received from Client...', text_data)
        
        if text_data == "close":
           await self.send(text_data="=>Connection close using self.close()")
           await self.close(code=3333)  # Close connection before sending any further messages
           return  # Ensure no more messages are sent after closing
            
        # self.send(bytes_data=data)  # To send Binary data
        await self.send(text_data="Message from server to Client")  # Send data to client

    def disconnect(self, close_code):
        """This handler is called when either connection to the client
        is lost, either from the client closing the connection, the server
        closing the connection, or loss of the socket."""
        print('Websocket Disconnected...', close_code)
