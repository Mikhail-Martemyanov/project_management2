from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from task.api.permissions import IsTaskForUser, IsManager, IsReadOnly
from task.api.serializers import TaskSerializer, TaskChangeStatusSerializer
from task.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsReadOnly,)

    @action(
        detail=True,
        methods=['get', 'put'],
        permission_classes=(IsTaskForUser,),
        serializer_class=TaskChangeStatusSerializer
    )
    def change_status(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskChangeStatusSerializer(task)

        return Response(serializer.data)

    @action(detail=True,
            methods=['get', 'put', 'delete'],
            permission_classes=(IsManager,),
            serializer_class=TaskSerializer
            )
    def change_task(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task)

        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=(IsManager,),
            serializer_class=TaskSerializer)
    def create_task(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskSerializer(task)

        return Response(serializer.data)
