from django.db import models

# Create your models here.

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=15000)

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lte=15000)

"""This Table always provide whose salary is greater than equal to 15000"""
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)
    objects=CustomManager1()

"""This Table always provide whose salary is less than equal to 15000"""
class ProxyEmployee1(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True