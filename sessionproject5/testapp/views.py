from django.shortcuts import render
from testapp.forms import *

# Create your views here.
def name_view(request):
    form=NameForm()
    return render(request,'testapp/name.html',{'form':form})

def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form,'name':name})

def friend_view(request):
    age=request.GET['age']
    request.session['age']=age
    name=request.session['name']
    form=FriendForm()
    return render(request,'testapp/friend.html',{'form':form,'name':name,'age':age})

def results_view(request):
    print(request.GET)
    # name=request.session['name']
    # age=request.session['age']
    friend = request.GET.get('friend', None)
    request.session['friend']=friend
    return render(request,'testapp/results.html')