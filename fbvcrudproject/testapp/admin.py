from django.contrib import admin
from testapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_diisplay=['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)
