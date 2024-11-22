from django.contrib import admin
# from testapp.models import Student,Teacher,Student1,ContactInfo1
from testapp.models import *
# Register your models here.
class ContactInfo1Admin(admin.ModelAdmin):
    fields=['name','email','address']

"""The model ContactInfo is abstract, so it cannot be registered with admin."""
# admin.site.register(ContactInfo)
admin.site.register(Student)
admin.site.register(Teacher)

"""Multi table Inheritance"""
admin.site.register(ContactInfo1,ContactInfo1Admin)
admin.site.register(Teacher1)
admin.site.register(Student1)

"""Multi level Inheritence"""
admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Manager)

"""multiple inheritance"""
admin.site.register(Parent1) 
admin.site.register(Parent2)
admin.site.register(Child)
