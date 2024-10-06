from django.urls import path
from . import views

urlpatterns=[
    path('images/',views.show_images),
    path('',views.index_views),
    path('demo/',views.movie_review)
]
