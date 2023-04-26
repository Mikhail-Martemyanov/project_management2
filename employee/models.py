from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    JOB_TITLE = [('manager', 'Менеджер'),
                 ('consultant', 'Консультант'),]
    name = models.CharField(max_length=100, verbose_name='ФИО сотрудника')
    job_title = models.CharField(max_length=10, choices=JOB_TITLE, default='consultant', verbose_name='Дожность')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='login', null=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотруднки'