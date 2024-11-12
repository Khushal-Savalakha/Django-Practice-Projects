from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/',views.name_view,name='u_name'),
    path('age/',views.age_view,name='u_age'),
    path('friend/',views.friend_view,name='u_friend'),
    path('result/',views.results_view,name='result')
]
