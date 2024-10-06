
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.HelloWorldView.as_view()),
    path('tt/',views.TemplateCBV.as_view()),
     path('tt2/',views.TemplateCBV2.as_view()),
]
