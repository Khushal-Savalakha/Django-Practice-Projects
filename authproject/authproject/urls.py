from django.contrib import admin
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page_view,name='home'),
    path('javaex/',views.java_page_view,name='java'),
    path('pyex/',views.python_page_view,name='python'),
    path('aptitudeex/',views.aptitude_page_view,name='aptitude'),
    path('accounts/',include('django.contrib.auth.urls'),name='login'),
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('logout/',views.logout_view),
    path('signup',views.signup_view,name='signup')
]
