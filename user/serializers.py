from rest_framework import serializers
from .models import *


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = '__all__'
        depth = 1
