from django.contrib import admin
from django.urls import include, path
import myapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]