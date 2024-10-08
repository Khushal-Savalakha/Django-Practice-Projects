from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.retrieve_view),
    path("specific/",views.retrieve_specific_column_view),
    path("aggr/",views.aggregation_view)
]
