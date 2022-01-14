from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *


# Parent ViewSet
class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all().order_by('id')
    serializer_class = ParentSerializer


# Child ViewSet
class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all().order_by('id')
    serializer_class = ChildSerializer
