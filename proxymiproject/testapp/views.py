from django.shortcuts import render
from testapp.models import *
# Create your views here.
def display_view(request):
    # employees=Employee.objects.all()
    employees=ProxyEmployee1.objects.all()
    return render(request,'testapp/index.html',{'emp':employees})