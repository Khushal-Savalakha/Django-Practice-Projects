from django.shortcuts import render
from testapp.models import FilterModel
# Create your views here.
def upper_data_view(request):
    records=FilterModel.objects.all() 
    return render(request,'testapp/upperdata.html',{'records':records})

