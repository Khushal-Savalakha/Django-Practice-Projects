from django.shortcuts import render
from .models import Chat,Group

# Create your views here.
def index(request,group_name):
    print("group name:",group_name)
    group=Group.objects.filter(name=group_name).first()
    print("--->data;",group)
    chats=[]
    if(group):
        chats=Chat.objects.filter(group=group)
        pass
    else:
        group=Group(name=group_name)
        group.save()
    return render(request,'app/index.html',{'groupname':group_name,'chats':chats})

"""
Django version 5.1.3, using settings 'gs10.settings'
Starting ASGI/Daphne version 4.1.2 development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
group name: indian
--->data; Group object (1)
HTTP GET /indian/ 200 [0.02, 127.0.0.1:46922]
WebSocket HANDSHAKING /ws/sc/indian/ [127.0.0.1:46944]
Websocket Connected.... {'type': 'websocket.connect'}
Channel Layer.... RedisChannelLayer(hosts=[{'host': 'localhost', 'port': 6379}])
Channel Name.... specific.7184cede32fb40ca97251ad5f54cc79c!8b2c15412c1b4775b679c1db3b0f48c8
Group Name: indian
WebSocket CONNECT /ws/sc/indian/ [127.0.0.1:46944]
HTTP GET /firebase-messaging-sw.js 301 [0.03, 127.0.0.1:46922]
group name: india
--->data; None
HTTP GET /india/ 200 [0.04, 127.0.0.1:48350]
WebSocket HANDSHAKING /ws/sc/india/ [127.0.0.1:48356]
Websocket Connected.... {'type': 'websocket.connect'}
Channel Layer.... RedisChannelLayer(hosts=[{'host': 'localhost', 'port': 6379}])
Channel Name.... specific.7184cede32fb40ca97251ad5f54cc79c!02506e2b6f4a4ed3adcc83e67835886b
Group Name: india
WebSocket CONNECT /ws/sc/india/ [127.0.0.1:48356]
WebSocket DISCONNECT /ws/sc/indian/ [127.0.0.1:46944]
Websocket Disconnected.... {'type': 'websocket.disconnect', 'code': 1001}
Channel Layer.... RedisChannelLayer(hosts=[{'host': 'localhost', 'port': 6379}])
Channel Name.... specific.7184cede32fb40ca97251ad5f54cc79c!8b2c15412c1b4775b679c1db3b0f48c8
"""