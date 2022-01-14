from rest_framework import serializers
from .models import *

# Parent Serializer (for the Parent model)


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'


# Child Serializer (for the Child model)
class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = '__all__'
        depth = 1
