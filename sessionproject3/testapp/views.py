from django.shortcuts import render
from testapp.forms import AddItemForm
# Create your views here.
def index_view(request):
    return render(request,'testapp/home.html')

def additems_view(request):
    form=AddItemForm()
    response=render(request,'testapp/add_item.html',{'form':form})
    if request.method=='POST':
        form=AddItemForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['item_name']
            quantity=form.cleaned_data['quantity']
            response.set_cookie(name,quantity,60)#data will be persisted for 60 seconds
    return response

def displayitems_view(request):
    return render(request,'testapp/display_items.html')