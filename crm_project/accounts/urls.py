from django.urls import path
from .views import (
    login_view, logout_view, redirect_based_on_role,
    HRDashboardView, AdminDashboardView,
    ContractorDashboardView, EmployeeDashboardView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", login_view, name="login"),  # ✅ Use our custom login view
    path("logout/", logout_view, name="logout"),
    path("redirect/", redirect_based_on_role, name="redirect_based_on_role"),
    path("dashboard/hr/", HRDashboardView.as_view(), name="hr_dashboard"),
    path("dashboard/admin/", AdminDashboardView.as_view(), name="admin_dashboard"),
    path("dashboard/contractor/", ContractorDashboardView.as_view(), name="contractor_dashboard"),
    path("dashboard/employee/", EmployeeDashboardView.as_view(), name="employee_dashboard"),
]
