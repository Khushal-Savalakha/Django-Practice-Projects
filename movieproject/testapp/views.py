from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def list_movies_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/listMovies.html',{'movies_list':movies_list})

def add_movies_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'testapp/addMovies.html',{'form':form})