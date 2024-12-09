from django.contrib import admin
from .models import *

class GenreAdmin(admin.ModelAdmin):
    list_display=['id','name']

class BookAdmin(admin.ModelAdmin):
    list_display=['id','title','author','description','published_date','price','is_active']

admin.site.register(Genre,GenreAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Department)
admin.site.register(Employee)
# Register your models here.
