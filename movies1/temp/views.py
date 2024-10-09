from django.shortcuts import render
from temp.models import Movie

def home(request):
    searchTerm = request.GET.get('searchMovie', '')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request,'MovieData.html', {'searchTerm': searchTerm, 'movies': movies})
