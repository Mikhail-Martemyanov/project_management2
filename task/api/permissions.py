from rest_framework import permissions

from employee.models import Employee


class IsTaskForUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.for_user_id == request.user.id


class IsManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user_employee = Employee.objects.get(id=request.user.id)
        return user_employee.job_title == 'manager'
