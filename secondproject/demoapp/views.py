from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.

def time_info_view(request):
    time=datetime.datetime.now()
    s='<h1>Hello current Date and Time:'+str(time)+'</h1>'
    return HttpResponse(s)

def datetimeinfo_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='<h1>Hello Friend,'
    if h<12:
        msg=msg+'Good Morning'
    elif h<16:
        msg=msg+'Good Afternoon'
    elif h<21:
        msg+='Good Evening'
    else:
        msg=msg+'Good Night'
    msg=msg+'</h1><hr>'
    msg=msg+'Now Server time is:'+str(date)+'</h1>'
    print(msg)
    return HttpResponse(msg)

