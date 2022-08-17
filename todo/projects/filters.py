from cProfile import label
from dataclasses import field
from pyexpat import model
from django_filters import rest_framework as filters
from .models import Projects, Todo


class ProjectsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Projects
        fields = ['name']


class TodoFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()
    project = filters.ModelChoiceFilter(queryset=Projects.objects.all())

    class Meta:
        model = Todo
        fields = ['project', 'created']
