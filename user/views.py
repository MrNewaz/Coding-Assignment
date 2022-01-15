from http.client import responses
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Parent ViewSet
class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all().order_by('id')
    serializer_class = ParentSerializer

    # Not Sure if I should exclude partial update or not.
    # http_method_names = ['get', 'post', 'put', 'delete']


# Child ViewSet
class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all().order_by('id')
    serializer_class = ChildSerializer
