from rest_framework import serializers
from .models import Supreceipt
from food.models import Food
from food.serializer import foodserializer

from sizes.models import Size
from sizes.serializer import sizeserializer



class SubPriceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Supreceipt
        fields="__all__"
    def create(self,validate_data):

        print("sondossssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        subprice_instance=Supreceipt.objects.create(**validate_data)
        size_object  =  validate_data.get('size_fk')

        size=size_object.sizee
        price=size_object.price
        
        
        subprice_instance.totalsupprice = price * subprice_instance.quantity
        print(subprice_instance.totalsupprice)
    
   
        
     
        subprice_instance.save()

        return subprice_instance
    