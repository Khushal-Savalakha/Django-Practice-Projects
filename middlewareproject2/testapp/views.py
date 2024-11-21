from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(request):
    return HttpResponse("<h1>Hello this function is from view function</h1>")

