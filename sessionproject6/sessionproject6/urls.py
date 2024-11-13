from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.add_item_view,name='add'),
    path('display/',views.display_item_view,name='display'),
    path("delete-items/", views.delete_items_view, name="delete_items"),
]
