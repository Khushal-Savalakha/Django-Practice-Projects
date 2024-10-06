from django.contrib import admin
from testapp.models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'ceo']

admin.site.register(Company, CompanyAdmin)
