from django.shortcuts import render
from testapp.models import Student22
# Create your views here.
def empdata_view(request):
    # student_list=Student22.objects.all()
    # print(student_list)
    # student_list=Student22.objects.filter(marks__lt=90)
    # student_list=Student22.objects.filter(name__startswith='M')
    # student_list=Student22.objects.all().order_by('marks')
    student_list=Student22.objects.all().order_by('-marks')
    # Removed unnecessary dictionary creation and directly passed 'student_list' to the render function
    return render(request, 'html/emp.html', {'student_list': student_list})