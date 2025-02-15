from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# ✅ Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("username", email)  # Use email as username
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


# ✅ Custom User Model
class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)

    ROLE_CHOICES = (
        ("HR", "HR"),
        ("Admin", "Admin"),
        ("Contractor", "Contractor"),
        ("Employee", "Employee"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Employee")

    objects = CustomUserManager()

    USERNAME_FIELD = "email"  # ✅ Use email for authentication
    REQUIRED_FIELDS = []  # ✅ Remove username from required fields

    def __str__(self):
        return self.email
