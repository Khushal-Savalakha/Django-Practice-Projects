# from django.shortcuts import render
# from .models import Chat,Group

# # Create your views here.
# def index(request,group_name):
#     print("group name:",group_name)
#     group=Group.objects.filter(name=group_name).first()
#     print("--->data;",group)
#     chats=[]
#     if(group):
#         chats=Chat.objects.filter(group=group)
#         pass
#     else:
#         group=Group(name=group_name)
#         group.save()
#     return render(request,'app/index.html',{'groupname':group_name,'chats':chats})


from django.shortcuts import render
from .models import Chat, Group

def index(request, group_name):
    print("Group Name:", group_name)
    group = Group.objects.filter(name=group_name).first()
    print("--->Group Data:", group)
    chats = []
    if group:
        chats = Chat.objects.filter(group=group).order_by('timestamp')  # Sort by time
    else:
        group = Group(name=group_name)
        group.save()
    return render(request, 'app/index.html', {'groupname': group_name, 'chats': chats})
