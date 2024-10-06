from django.shortcuts import render
from django.urls import reverse_lazy
from testapp.models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# def list_view(request):
#     books_list=Book.objects.all()
#     return render(request,'testapp/books.html',{'books_list':books_list})


class BookListView(ListView):
    model=Book
    #default template file:book_list.html
    #default context object name:book_list.html
    # template_name='testapp/books.html'
    context_object_name='books'

class BookDetailView(DetailView):
    model=Book
    #default template file:book_detail.html
    #default context object name:book or object

class BookCreateView(CreateView):
    model=Book
    fields='__all__'

class BookUpdateView(UpdateView):
    model=Book
    fields=('title','pages','price')
    #the default template is book_form.html

class BookDeleteView(DeleteView):
    model=Book
    success_url=reverse_lazy('list')