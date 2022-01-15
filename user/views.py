from http.client import responses
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Parent ViewSet
class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all().order_by('id')
    serializer_class = ParentSerializer

    """
    Folowing the instructions from the assignment, 
    only alowing the GET, POST, PUT and DELETE methods. (Get is allowed so that the routes can be tested)
    """
    http_method_names = ['get', 'post', 'put', 'delete']


# Child ViewSet
class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all().order_by('id')
    serializer_class = ChildSerializer

    """
    Folowing the instructions from the assignment, 
    only alowing the GET, POST, PUT and DELETE methods. (Get is allowed so that the routes can be tested)
    """
    http_method_names = ['get', 'post', 'put', 'delete']
