from django.contrib import admin

from employee.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_title', 'user')


admin.site.register(Employee, EmployeeAdmin)
