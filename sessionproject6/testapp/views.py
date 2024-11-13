from django.shortcuts import render
from testapp.forms import AddItemForm
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

def add_item_view(request):
    form=AddItemForm()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render(request,'testapp/additem.html',{'form':form})

def display_item_view(request):
    return render(request,'testapp/displayitems.html')

def delete_items_view(request):
    if request.method == "POST":
        items_to_delete = request.POST.getlist("items_to_delete")
        for item_key in items_to_delete:
            if item_key in request.session:
                del request.session[item_key]
        # Save session after modifying it
        request.session.modified = True
    return redirect(reverse("display"))