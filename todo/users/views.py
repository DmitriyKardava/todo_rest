from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import TodoUser
from .serializers import TodoUserModelSerializer


class TodoUserCustomViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class TodoUserModelViewSet(viewsets.ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer
