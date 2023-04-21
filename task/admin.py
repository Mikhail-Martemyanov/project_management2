from django.contrib import admin

from task.models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('for_user', 'text_task', 'author_task', 'status')


admin.site.register(Task, TaskAdmin)
