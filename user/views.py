from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# Create your views here.


class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all().order_by('id')
    serializer_class = ParentSerializer


class ChildViewSet(ModelViewSet):
    queryset = Child.objects.all().order_by('id')
    serializer_class = ChildSerializer
