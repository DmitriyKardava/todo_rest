from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Projects, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

