from django.contrib import admin
from testapp.models import Job
from testapp.models import Employee
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display=['ename','esalary']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']


admin.site.register(Job,JobAdmin)
admin.site.register(Employee,EmployeeAdmin)