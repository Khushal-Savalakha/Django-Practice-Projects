from django.contrib import admin
from django.urls import path,include
import app 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('app.urls'))
]
