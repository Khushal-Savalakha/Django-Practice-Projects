from django.contrib import admin
from .models import Page,Page2,Page3
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_publish_date','user']


@admin.register(Page2)
class Page2Admin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_publish_date','user']

@admin.register(Page3)
class Page3Admin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_publish_date','user']