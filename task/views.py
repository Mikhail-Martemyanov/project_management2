from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response


from task.api.permissions import IsManagerOrReadOnly
from task.api.serializers import TaskSerializer, TaskChangeStatusSerializer
from task.models import Task


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    @action(detail=False, methods=['get'])
    def task(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    @action(detail=True, methods=['get', 'put'])
    def change(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskChangeStatusSerializer(task)

        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            print('1')
            permission_classes = (IsAuthenticated,)

        else:
            print('3')
            permission_classes = (IsManagerOrReadOnly, )

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):

        if self.action == 'update':

            self.serializer_class = TaskChangeStatusSerializer
        else:
            self.serializer_class = TaskSerializer

        assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )

        return self.serializer_class
