from django.shortcuts import render,HttpResponse
from .models import Book,Employee,Department,Genre


def index(request):
    books=Book.objects.all()
    for book in books:
        # print(book)#it tooks only 1 query to fetch all Book data
        """Charlie Chaplin-->34.00
        Journey To the West-->89.00
        Aladin-->50.00"""
        print(book.genres.all())#It requires 8 requires 3 queries individually to fetch data of each Book's genre
        """<QuerySet [<Genre: Science Friction>, <Genre: Romance>, <Genre: Comedy>]>
        <QuerySet [<Genre: Fight>]>
        <QuerySet [<Genre: Magic>]>"""
    return HttpResponse("<h1>It shows Books Data in backend</h1>")

def index2(request):
    books=Book.objects.prefetch_related("genres")
    for book in books:
        print(book.genres.all())
        """<QuerySet [<Genre: Science Friction>, <Genre: Romance>, <Genre: Comedy>]>
        <QuerySet [<Genre: Fight>]>
        <QuerySet [<Genre: Magic>]>"""
    return HttpResponse("<h1>It shows Books Data with genre using prefetch_related </h1>")


def reverse_data_fetching(request):
    genres=Genre.objects.all()
    for genre in genres:
        print(genre.name)
        print(genre.book_data.all())
        
    return HttpResponse("<h1>It shows Books Data with genre use . </h1>")

def reverse_data_fetching2(request):
    # Prefetch related Book objects for each Genre
    genres = Genre.objects.all().prefetch_related('book_data')  # 'book_data' is the related name for the ManyToManyField
    for genre in genres:
        print(genre.name)
        # Now, 'book_data.all()' will not hit the database for each genre, as it's already prefetched
        print(genre.book_data.all())
        
    return HttpResponse("<h1>It shows Books Data with genre using prefetch_related</h1>")
def home(request):
    employees=Employee.objects.all()
    for employee in employees:
        print(employee.name,":",employee.department.name)
    return HttpResponse("<h1>It shows Employee table data which uses ForeignKey</h1>")


def home2(request):
    employees=Employee.objects.all().select_related('department')
    for employee in employees:
        print('-->',employee.name,":",employee.department.name)
    return HttpResponse("<h1>It shows Employee table data which uses ForeignKey using Select_releted</h1>")