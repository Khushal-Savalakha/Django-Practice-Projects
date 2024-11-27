from django.db import models


# Custom manager to define a default queryset ordering
class CustomManager(models.Manager):
    def get_queryset(self):
        # Returns the queryset ordered by 'eno'
        return super().get_queryset().order_by("eno")
    
    def get_emp_sal_range(self,minsal,maxsal):
        qs=super().get_queryset().filter(esal__range=(minsal,maxsal))
        return qs
    
    def get_emp_sorted_by(self,param):
        qs=super().get_queryset().order_by(param)
        return qs


# Employee model with a custom manager for ordered results
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)
    """ Assigning a custom manager to override the default queryset behavior
     By using CustomManager here, we ensure that all queries on the Employee model
     are automatically ordered by 'eno', without needing to explicitly specify it
     in every query."""
    objects = CustomManager()
