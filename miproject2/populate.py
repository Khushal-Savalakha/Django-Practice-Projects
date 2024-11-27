import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','miproject2.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
from random import *
faker=Faker()

def populate(n):
    for i in range(n):
        feno=faker.random_int(min=1000,max=9999)
        fname=faker.name()
        fsal=faker.random_int(min=10000,max=100000)
        faddr=faker.city()
        emp=Employee(eno=feno,ename=fname,esal=fsal,eaddr=faddr)
        emp.save()
populate(100)