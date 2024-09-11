from rest_framework import serializers
from .models import Food
from restaurant.models import Restaurant
from sizes.serializer import sizeserializer
from sizes.models import Size
from rest_framework.response import Response

class foodserializer(serializers.ModelSerializer):
    sizes = sizeserializer(many=True, write_only = True)

    class Meta:
        model=Food
        fields="__all__"


    def create(self, validated_data):
        sizes_data = validated_data.pop('sizes', [])
        food = Food.objects.create(**validated_data)
        restaurent = food.res_fk

        for size_data in sizes_data:
            Size.objects.create(food_fk=food, owner_fk =restaurent.owner_fk,**size_data)
        return food
   
