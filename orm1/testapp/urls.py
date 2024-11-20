from django.urls import path
from testapp import views

urlpatterns = [
    path('emp_data',views.show_data),
    path('filter_data',views.filtered_data),
    path('emp_info',views.employee_data),
    path('aggregate',views.aggregation_view),
    path('updated',views.updated_data)
]
