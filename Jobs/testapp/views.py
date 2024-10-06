from django.shortcuts import render
from testapp.models import HydJobs,BangloreJobs,PuneJobs
# Create your views here.

def home_views(request):
    return render(request,'testapp/index.html')

def hyd_views(request):
    jobs_list=HydJobs.objects.all()
    return render(request,'testapp/hyd.html',{'jobs_list':jobs_list})