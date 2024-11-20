from django.db import models

# Create your models here.
class Job(models.Model):
    ename=models.CharField(max_length=30)
    esalary=models.IntegerField()
    
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)