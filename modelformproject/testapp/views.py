from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.

def student_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Record Inserted into database Successfull')
    return render(request,'testapp/studentform.html',{'form':form})