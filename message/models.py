from django.db import models


# Create your models here.
class Message(models.Model):
    author_message = models.ForeignKey('employee.Employee', on_delete=models.SET_NULL, verbose_name='Автор сообщения', null=True)
    text_message = models.TextField(verbose_name='текст сообщения')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='время публикации')

    class Meta():
        verbose_name = 'собщение'
        verbose_name_plural = 'собщений'
