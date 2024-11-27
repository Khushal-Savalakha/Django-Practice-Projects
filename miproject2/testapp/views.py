from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def display_view(request):
    # emp_list=Employee.objects.all()
    # emp_list=Employee.objects.get_emp_sal_range(19000,20000)
    # emp_list=Employee.objects.get_emp_sorted_by('ename')
    emp_list=Employee.objects.get_emp_sorted_by('-esal')
    return render(request,'testapp/index.html',{'emp':emp_list})

