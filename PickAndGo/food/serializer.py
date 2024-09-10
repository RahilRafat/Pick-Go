from rest_framework import serializers
from .models import Food
from restaurant.models import Restaurant

class foodserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Food
        fields="__all__"