from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    # print('-------------------------->')
    print(type(request))
    s='s'
    return HttpResponse(s)

