from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from employee.models import Employee
from task.api.permissions import IsTaskForUser, IsManager
from task.api.serializers import TaskSerializer, TaskChangeStatusSerializer
from task.models import Task


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    # serializer_class = TaskSerializer

    @action(detail=False, methods=['get'])
    def task(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    @action(detail=True, methods=['get', 'put'])
    def change_status(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskChangeStatusSerializer(task)

        return Response(serializer.data)

    @action(detail=True, methods=['get', 'put', 'delete'])
    def change_task(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    @action(detail=True, methods=['get', 'post'])
    def create_task(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    def get_permissions(self):
        user_id = self.request.user.id
        queryset_job_title = Employee.objects.get(user=user_id).job_title

        if self.action == 'update' and queryset_job_title == 'manager':
            permission_classes = (IsManager,)

        elif self.action == 'destroy' or self.action == 'create':
            permission_classes = (IsManager,)

        elif self.action == 'task-status':
            permission_classes = (IsTaskForUser,)

        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = (IsAuthenticated,)

        else:
            permission_classes = (IsTaskForUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):

        user_id = self.request.user.id
        queryset_job_title = Employee.objects.get(user=user_id).job_title  # получаем должность юзера от кого запрос
        if (queryset_job_title == 'manager' and self.action == 'update') or queryset_job_title == 'manager':
            self.serializer_class = TaskSerializer

        elif self.action == 'create' and queryset_job_title == 'manager':
            self.serializer_class = TaskSerializer

        elif self.action == 'update':
            self.serializer_class = TaskChangeStatusSerializer
        else:
            self.serializer_class = TaskSerializer

        assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )

        return self.serializer_class
