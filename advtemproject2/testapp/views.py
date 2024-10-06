from django.shortcuts import render
# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movies_page_view(request):
    return render(request,'testapp/movies.html')

def politics_page_view(request):
    return render(request,'testapp/politics.html')

def sports_page_view(request):
    return render(request,'testapp/sports.html')