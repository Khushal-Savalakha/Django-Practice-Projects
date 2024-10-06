from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from testapp.models import Company
# Create your views here.

class CompanyListView(ListView):
    model=Company
#default tenplate file:company_list.html
#default context object Name:comapny_list

class CompanyDetailView(DetailView):
    model=Company
    #default template file:company_detail.html
    #default context object name:Company or object

class CompanyCreateView(CreateView):
    model=Company
    # fields=('name','location','ceo')
    fields='__all__'
    #default template file:company_form.html
