from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=10)
    course = models.CharField(max_length=12)
    start_time = models.CharField(max_length=20)
    finish_time = models.CharField(max_length=20)
    time_minute = models.CharField(max_length=10)