from rest_framework import serializers
from .models import Supreceipt
from food.models import Food
from food.serializer import foodserializer

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

    def create(self,validate_data):

        print("sondossssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        subprice_instance=Supreceipt.objects.create(**validate_data)
        size_object  =  validate_data.get('size_fk')

        size=size_object.size
        price=size_object.price
        
        
        subprice_instance.totalsupprice = price * subprice_instance.quantity
        print(subprice_instance.totalsupprice)
    
   
        
     
        subprice_instance.save()

        return subprice_instance
    