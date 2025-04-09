from rest_framework import serializers
from .models import Food
from restaurant.models import Restaurant
from sizes.serializer import sizeserializer
from sizes.models import Size
from rest_framework.response import Response

class FoodSerializer(serializers.ModelSerializer):
   

    class Meta:
        model=Food
        fields = ['id', 'name', 'description', 'res_fk', 'img']
    

    