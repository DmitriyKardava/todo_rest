from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TodoUser


class TodoUserModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = TodoUser
       fields = [
        'id',
        'username', 
        'first_name', 
        'last_name', 
        'email',
        ]