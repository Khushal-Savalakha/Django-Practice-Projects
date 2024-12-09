from django.contrib import admin
from django.urls import path,include
from debug_toolbar.toolbar import debug_toolbar_urls
from django_queries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('data/',views.index),
    path('data2/',views.index2),
    path('home/',views.home),
    path('home2/',views.home2),
    path('reverse_data/',views.reverse_data_fetching),
    path('reverse_data2/',views.reverse_data_fetching2)

]
