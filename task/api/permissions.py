from rest_framework import permissions

from employee.models import Employee


class IsManagerOrReadOnly(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True

    def has_object_permission(self, request, view, obj):
        user_employee = Employee.objects.get(id=request.user.id)

        return user_employee.job_title == 'manager' or obj.for_user_id == request.user.id


# class IsTaskForMe(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.for_user_id == request.user.id
