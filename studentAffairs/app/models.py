from django.db import models


CHOICE = [('Male', 'Male'),
          ('Female', 'Female')]
STATUS = [('Active', 'Active'), ('Inactive', 'Inactive')]

DEPARTMENT = [('General', 'General'), ('CS', 'CS'), ('IS', 'IS'),
              ('DS', 'DS'), ('AI', 'AI'), ('IT', 'IT')]

LEVEL = [(1, 1), (2, 2), (3, 3), (4, 4)]

NATIONALITY = [('Algerian', 'Algerian'),
               ('Bahraini', 'Bahraini'),
               ('Comorian', 'Comorian'),
               ('Djiboutian', 'Djiboutian'),
               ('Egyptian', 'Egyptian'),
               ('Emirati', 'Emirati'),
               ('Iraqi', 'Iraqi'),
               ('Jordanian', 'Jordanian'),
               ('Kuwaiti', 'Kuwaiti'),
               ('Lebanese', 'Lebanese'),
               ('Libyan', 'Libyan'),
               ('Mauritanian', 'Mauritanian'),
               ('Moroccan', 'Moroccan'),
               ('Omani', 'Omani'),
               ('Palestinian', 'Palestinian'),
               ('Qatari', 'Qatari'),
               ('Saudi Arabian', 'Saudi Arabian'),
               ('Somali', 'Somali'),
               ('Sudanese', 'Sudanese'),
               ('Syrian', 'Syrian'),
               ('Tunisian', 'Tunisian'),
               ('Yemeni', 'Yemeni')]


class Student(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10, choices=CHOICE)
    status = models.CharField(max_length=10, choices=STATUS)
    level = models.IntegerField(choices=LEVEL)
    department = models.CharField(
        max_length=30, choices=DEPARTMENT, default=None)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=None)
    nationalid = models.IntegerField(default=None)
    nationality = models.CharField(max_length=50, choices=CHOICE)
    birthdate = models.DateTimeField(default=None)
