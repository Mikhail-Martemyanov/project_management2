from functools import partial

from rest_framework import viewsets, status
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
        methods=['put'],
        permission_classes=(IsTaskForUser,),
        serializer_class=TaskChangeStatusSerializer)
    def change_status(self, request, *args, **kwargs):
        task = self.get_object()
        serializer = TaskChangeStatusSerializer(instance=task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @action(detail=True,
            methods=['put', 'delete'],
            permission_classes=(IsManager,),
            serializer_class=TaskSerializer
            )
    def change_task(self, request, *args, **kwargs):
        task = self.get_object()

        if request.method == 'DELETE':
            self.perform_destroy(task)
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @action(detail=False, methods=['post'],
            permission_classes=(IsManager,),
            serializer_class=TaskSerializer)
    def create_task(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
