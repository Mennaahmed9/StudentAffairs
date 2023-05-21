from django.db import models


CHOICE = [('Male', 'Male'),
          ('Female', 'Female')]
STATUS = [('Active', 'Active'),( 'Inactive','Inactive')]

DEPARTMENT = [('General', 'General'), ('CS', 'CS'), ('IS', 'IS'),
          ('DS', 'DS'), ('AI','AI'), ('IT', 'IT')]


class Student(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10, choices=CHOICE)
    status = models.CharField(max_length=10, choices=STATUS)
    level = models.IntegerField()
    department = models.CharField(max_length=30, choices=DEPARTMENT)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    nationalid = models.IntegerField(max_length=5)
    nationality = models.CharField(max_length=50)
    birthdate = models.DateTimeField()

