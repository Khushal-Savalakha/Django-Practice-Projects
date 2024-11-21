from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(request):
    print(10/0)
    return HttpResponse("<h1>Hello this is from view function.</h1>")
