from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskChangeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('status', )
