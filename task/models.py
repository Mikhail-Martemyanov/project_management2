from django.db import models


# Create your models here.
class Task(models.Model):
    for_user = models.OneToOneField('employee.Employee', on_delete=models.SET_NULL,
                                    null=True,
                                    verbose_name='Выпоняет')  # id кому адресована задача

    text_task = models.TextField(verbose_name='Задача')

    author_task = models.ForeignKey('employee.Employee', on_delete=models.SET_NULL,
                                    null=True, related_name='author_tasks',
                                    verbose_name='Задание выдал')  # id автора задачи

    status = models.BooleanField(default=False, verbose_name='Статус')

    class Meta():
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
