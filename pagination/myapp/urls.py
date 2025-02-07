from django.urls import path
from . import views
from .views import advanced_pagination, BlogPostListView

urlpatterns = [
    path('paginate/', views.paginate_numbers, name='paginate_numbers'),
    path('advanced-paginate/', advanced_pagination, name='advanced_pagination'),
    path('blog-posts/', BlogPostListView.as_view(), name='blogpost_list'),
]