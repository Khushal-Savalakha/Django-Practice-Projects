from django.shortcuts import render
from testapp.forms import LoginForm
import datetime
# Create your views here.
def home_view(request):
    form=LoginForm()
    return render(request,'testapp/home.html',{'form':form})


def date_time_view(request):
    name = request.GET['name']
    password = request.GET['password']
    response = render(request, 'testapp/date_time.html', {'name': name})
    
    # Set individual cookies for 'name' and 'password'
    response.set_cookie('name', name)
    response.set_cookie('password', password)
    
    return response

def result_view(request):
    name=request.COOKIES['name']
    date_time=datetime.datetime.now()
    return render(request,'testapp/result.html',{'name':name,'date_time':date_time})