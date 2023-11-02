from rest_framework import serializers
from .models import TaskForce, TaskForceApplication

class TaskForceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskForce
        fields = '__all__'


class TaskForceApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskForceApplication
        fields = '__all__'
    

