from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from .models import Restaurant


class resturantserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Restaurant
        fields="__all__"