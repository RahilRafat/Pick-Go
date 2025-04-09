from rest_framework import serializers
from .models import Supreceipt
from food.models import Food
from food.serializer import FoodSerializer

from sizes.models import Size
from sizes.serializer import sizeserializer
from  food.models import Food
from restaurant.models import Restaurant
from users.models import CustomUser
from  sizes.models import Size
from totalreceipt.models import TotalReciept


class SubPriceSerializer(serializers.ModelSerializer):

    total_reciet_fk = serializers.PrimaryKeyRelatedField(
        queryset=TotalReciept.objects.all(),
        required=False,  
        allow_null=True
    )
    food_fk= serializers.PrimaryKeyRelatedField(queryset = Food.objects.all())
    size_fk= serializers.PrimaryKeyRelatedField(queryset = Size.objects.all())


    class Meta:
        model=Supreceipt
        fields="__all__"

   
        
    def create(self, validated_data):
        try:
            
            food_fk = validated_data.get('food_fk')
            size_fk = validated_data.get('size_fk')
            total_reciet_fk = validated_data.get('total_reciet_fk')

            if not food_fk:
                raise serializers.ValidationError("Food information is required.")
            if not size_fk:
                raise serializers.ValidationError("Size information is required.")
            
            
            if not total_reciet_fk:
                raise serializers.ValidationError("Total receipt information is required.")
            
            quantity = validated_data.get('quantity', 1)
            if quantity <= 0:
                raise serializers.ValidationError("Quantity must be a positive integer.")
            
            
            subprice_instance = Supreceipt.objects.create(**validated_data)

           
            size = size_fk.size
            price = size_fk.price
            subprice_instance.totalsupprice = price * quantity

            subprice_instance.save()

            return subprice_instance
        
        except Exception as e:
           
            raise serializers.ValidationError(f"Error creating Subreceipt: {e}")
        


class ListSubPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supreceipt
        fields = ['res_fk','food_fk', 'size_fk', 'quantity', 'totalsupprice']