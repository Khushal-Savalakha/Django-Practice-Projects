from django.contrib import admin
from django.urls import path,include
import testapp 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',include('testapp.urls'))
]
