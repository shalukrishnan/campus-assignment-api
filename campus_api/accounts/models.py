from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('ME', 'Mechanical'),
    ]

    YEAR_CHOICES = [
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    ]

    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email', 'department', 'year']

    def __str__(self):
        return self.username