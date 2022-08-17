from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .models import Projects, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from .filters import ProjectsFilter, TodoFilter


class ProjectsLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectsLimitOffsetPagination
    filterset_class = ProjectsFilter


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    # queryset = Todo.objects.filter(is_active=True)
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()
        return Response(status=status.HTTP_200_OK)
