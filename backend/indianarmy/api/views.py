from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TaskForce, TaskForceApplication
from .serializers import TaskForceSerializer, TaskForceApplicationSerializer 



class TaskForceListCreateView(generics.ListCreateAPIView):
    queryset = TaskForce.objects.all()
    serializer_class = TaskForceSerializer

class TaskForceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskForce.objects.all()
    serializer_class = TaskForceSerializer


class TaskForceApplicationListCreateView(generics.ListCreateAPIView):
    queryset = TaskForceApplication.objects.all()
    serializer_class = TaskForceApplicationSerializer

   