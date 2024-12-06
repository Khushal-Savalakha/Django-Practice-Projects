#Topic -Consumer

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        """This handler is called when client initially opens a connnection and is about to finish
          the Websocket handshake"""
        print('WEBSOCKET Connected.....',event)
        self.send(
            {
                'type':'websocket.accept'
            }
        )

    def websocket_receive(self,event):
        """The handler is called when data received from client"""
        print('MESSAGE Received.....',event)
        print('Message is ',event['text'])

    def websocket_diconnect(self,event):
        """The handler is called when either connection to client os lost or client
        closing the connection,the server closing the connection,or loss of the socket"""
        print('WEBSOCKET Disconnected.....',event)
        raise StopConsumer()



class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self,event):
        """This handler is called when client initially opens a connnection and is about to finish
          the Websocket handshake"""
        await self.send(
            {
                'type':'websocket.accept'
            }
        )
        print('WEBSOCKET Connected.....',event)
        

    async def websocket_receive(self,event):
        """The handler is called when data received from client"""
        print('MESSAGE Received.....',event)
        print('Message is ',event['text'])


    async def websocket_diconnect(self,event):
        """The handler is called when either connection to client os lost or client
        closing the connection,the server closing the connection,or loss of the socket"""
        print('WEBSOCKET Disconnected.....',event)
        raise StopConsumer()