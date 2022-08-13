from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Projects, Todo


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

