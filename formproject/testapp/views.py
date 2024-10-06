from django.shortcuts import render
from testapp.forms import StudentForm
# Create your views here.

def student_input_view(request):
    submitted=False
    sname=''
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printinfg data')
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])
            sname=form.cleaned_data['name']
            submitted=True
    form=StudentForm()
    return render(request,'testapp/input.html',{'form':form,'submitted':submitted,'sname':sname})
