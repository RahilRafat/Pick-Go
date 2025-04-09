from django.shortcuts import render
from rest_framework import serializers
from .models import Restaurant


class ResturantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Restaurant
        fields="__all__"

class ResturantNameserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Restaurant
        fields=['id', 'name']
