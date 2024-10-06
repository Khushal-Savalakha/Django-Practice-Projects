from django.contrib import admin
from testapp.models import Student22
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','marks']

admin.site.register(Student22,StudentAdmin)