from django.shortcuts import render
from .models import Employee
from django.db.models import Q
from django.db.models.functions import Lower

def retrieve_view(request):
    # emp_list=Employee.objects.all()
    # emp_list=Employee.objects.filter(esal__lt=25000)
    # emp_list=Employee.objects.filter(esal__gte=25000)
    # emp_list=Employee.objects.filter(id__in=[1,3,5])
    # emp_list=Employee.objects.filter(ename__startswith='A')
    # emp_list=Employee.objects.filter(ename__endswith='t')
    # emp_list=Employee.objects.filter(esal__range=(20000,30000))
    # emp_list = Employee.objects.filter(ename__startswith="D") | Employee.objects.filter(
    #     esal__lt=25000
    # )
    # emp_list=Employee.objects.filter(Q(ename__startswith="A") | Q(esal__lt=25000))
    # emp_list = Employee.objects.filter(ename__startswith="A",esal__lt=25000)
    # emp_list=Employee.objects.exclude(ename__startswith="A")
    # emp_list = Employee.objects.filter(~Q(ename__startswith="A"))
    # emp_list = Employee.objects.all().order_by('eno')#ascending order
    # emp_list = Employee.objects.all().order_by('-eno')#descending order
    # emp_list = Employee.objects.all().order_by('-esal')
    # emp_list = Employee.objects.all().order_by(Lower('ename'))
    # Union operation
    q1=Employee.objects.filter(ename__startswith="J")
    q2=Employee.objects.filter(esal__lt=30000)
    q3=q1.union(q2)
    emp_list=q3
    return render(request, "testapp/index.html", {"emp_list": emp_list})


def retrieve_specific_column_view(request):
    # emp_list=Employee.objects.all().values_list("ename","esal")
    # emp_list=Employee.objects.all().values("ename","esal")
    emp_list = Employee.objects.all().only("ename", "esal")
    return render(request, "testapp/specific_columns.html", {"emp_list": emp_list})


from django.db.models import Avg, Sum, Min, Max, Count

# def aggregation_view(request):
#     avg1=Employee.objects.all().aggregate(Avg("esal"))
#     # my_dict={'avg1':avg1}
#     # print(my_dict)
#     # return render(request, "testapp/aggregation.html", {"my_dict":my_dict})
#     print(avg1)
#     return render(request, "testapp/aggregation.html",{"avg1":avg1["esal__avg"]})


def aggregation_view(request):
    avg = Employee.objects.all().aggregate(Avg("esal"))
    max = Employee.objects.all().aggregate(Max("esal"))
    min = Employee.objects.all().aggregate(Min("esal"))
    sum = Employee.objects.all().aggregate(Sum("esal"))
    count = Employee.objects.all().aggregate(Count("esal"))
    return render(
        request,
        "testapp/aggregation.html",
        {
            "avg": avg["esal__avg"],
            "max": max["esal__max"],
            "min": min["esal__min"],
            "sum": sum["esal__sum"],
            "count": count["esal__count"],
        },
    )
