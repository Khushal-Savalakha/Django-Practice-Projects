from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from .permissions import HRRequiredMixin, AdminRequiredMixin, ContractorRequiredMixin, EmployeeRequiredMixin
from accounts.models import CustomUser  # ✅ Ensure correct import


# ✅ FIXED LOGIN FUNCTION
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email").strip().lower()  # Normalize email
        password = request.POST.get("password")

        print(f"Attempting login for: {email}")  # Debugging

        try:
            user = CustomUser.objects.get(email=email)
            print(f"User found: {user}")
        except CustomUser.DoesNotExist:
            print("User not found!")
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})

        # Authenticate user
        user = authenticate(request, username=user.email, password=password)
        print(f"Authentication result: {user}")

        if user and user.is_active:
            print("User authenticated successfully!")
            login(request, user)
            return redirect("redirect_based_on_role")  # Redirect after login
        else:
            print("Authentication failed!")
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")


# ✅ LOGOUT FUNCTION
def logout_view(request):
    logout(request)
    return redirect("login")


# ✅ REDIRECTION BASED ON USER ROLE
@login_required
def redirect_based_on_role(request):
    """Redirect users to their role-specific dashboard after login."""
    role_redirects = {
        "HR": "hr_dashboard",
        "Admin": "admin_dashboard",
        "Contractor": "contractor_dashboard",
        "Employee": "employee_dashboard",
    }
    return redirect(role_redirects.get(request.user.role, "login"))


# ✅ REGISTRATION FUNCTION
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("redirect_based_on_role")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# ✅ DASHBOARD VIEWS
class HRDashboardView(LoginRequiredMixin, HRRequiredMixin, TemplateView):
    template_name = "hr_dashboard.html"

class AdminDashboardView(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = "admin_dashboard.html"

class ContractorDashboardView(LoginRequiredMixin, ContractorRequiredMixin, TemplateView):
    template_name = "contractor_dashboard.html"

class EmployeeDashboardView(LoginRequiredMixin, EmployeeRequiredMixin, TemplateView):
    template_name = "employee_dashboard.html"
