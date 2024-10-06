from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    #in form class defining size is optional but in model class it is mandatory
    marks=models.IntegerField()
