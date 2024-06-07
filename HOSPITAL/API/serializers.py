from rest_framework import serializers
from .models import*

class CreatePATIENTserializer(serializers.Serializer):
    name = serializers.CharField(max_length= 100)
    age = serializers.IntegerField() 
    gender = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    p_mobile = serializers.IntegerField()


class updateAddressPatientserializer(serializers.Serializer):
    gender = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)