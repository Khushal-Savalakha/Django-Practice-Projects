from django.shortcuts import render
from testapp.models import Job
from django.db.models import Q
from testapp.models import Employee
from django.db.models import F
from django.db.models.functions import Concat


# Create your views here.
def show_data(request):
    data=Job.objects.all()
    return render(request,'testapp/ShowData.html',{'emp_data':data})

def filtered_data(request):
    """here esalary__gt is fieldlookup esalary:field and __gt:lookup type"""
    # data=Job.objects.filter(esalary__gt=15000)
    # data=Job.objects.filter(esalary__lte=10000)#method to query the Employee model with certain conditions.
    # data=Job.objects.filter(ename__iexact='khushal')
    # data=Job.objects.filter(ename__endswith='arth')

    # Using Q for complex queries

    """How to use & and | operator"""
    # data=Job.objects.filter(Q(Q(ename__iexact='hetarth')|Q(esalary__gte=20000)) & Q(esalary__lte=25000))
    # data=Job.objects.filter(Q(Q(ename__iexact='hetarth')|Q(esalary__gte=20000)) & Q(esalary__lt=21000,esalary__gt=10000))
    
    """Use of NOR operator"""
    # data=Job.objects.filter(~Q(esalary__lt=45000,esalary__gt=5000))
    # data=Job.objects.exclude(Q(esalary__lt=45000,esalary__gt=5000))

    """How to use UNION oprator"""
    Q1=Job.objects.filter(ename__exact="hetarth")
    Q2=Job.objects.filter(esalary__lte=5000)
    data=Q1.union(Q2)

    return render(request,'testapp/ShowData.html',{'emp_data':data})

def employee_data(request):
    """How to select only some columns in the queryset"""
    # data=Employee.objects.all()
    # data=Employee.objects.all().values_list("ename","esal")#[tuple,tuples]
    # data=Employee.objects.all().values("ename","esal")
    data=Employee.objects.all().only("ename","esal")#
    print(data)
    return render(request,'testapp/EmployeeData.html',{'emp_data':data})


from django.db.models import Avg,Sum,Min,Max,Count

def aggregation_view(request):
    """Aggregate Functions"""
    avg=Employee.objects.all().aggregate(Avg("esal"))
    max=Employee.objects.all().aggregate(Max("esal"))
    min=Employee.objects.all().aggregate(Min("esal"))
    sum=Employee.objects.all().aggregate(Sum("esal"))
    count=Employee.objects.all().aggregate(Count("esal"))
    return render(
        request,
        "testapp/aggregate.html",
        {
            "avg": avg["esal__avg"],
            "max": max["esal__max"],
            "min": min["esal__min"],
            "sum": sum["esal__sum"],
            "count":count["esal__count"],
        },
    )


def updated_data(request):
    """How to use F() Expression"""
    word="KKK"
    # Employee.objects.update(esal=F('esal')+20)
    Employee.objects.update(ename=Concat(F('ename'),F('eaddr')))
    #Here we can't directly append any character or word it will always find any field in database
    data=Employee.objects.all()
    return render(request,'testapp/full_emp_data.html',{'emp':data})