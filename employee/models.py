from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    JOB_TITLE = [('manager', 'Менеджер'),
                 ('consultant', 'Консультант'),]
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=10, choices=JOB_TITLE, default='consultant')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
