from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    """
    Represents a page created by a user. Each user can create only one page.
    The associated User instance is deleted when the Page instance is deleted.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


class Page2(models.Model):
    """
    Represents a page created by a user with added protection.
    The associated User instance is protected and cannot be deleted 
    if this Page2 instance exists.
    """
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


class Page3(models.Model):
    """
    Represents a page associated with staff users only.
    This model restricts the available users to those where is_staff=True.
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff': True}
    )
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
