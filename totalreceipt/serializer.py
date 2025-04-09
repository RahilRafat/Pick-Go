from rest_framework import serializers
from .models import TotalReciept
from supreceipt.models import Supreceipt
from supreceipt.serializer import SubPriceSerializer
from users.models import CustomUser
from restaurant.serializer import ResturantNameserializer
from supreceipt.serializer import ListSubPriceSerializer

class RecieptSerializer(serializers.ModelSerializer):
    subprice_data = SubPriceSerializer(many=True, required=False)
    user_fk= serializers.PrimaryKeyRelatedField(queryset = CustomUser.objects.all())

    class Meta:
        model=TotalReciept
        fields="__all__"



    def create(self ,validate_data):
        
        subprice_data_items = validate_data.pop('subprice_data', [])        
        Reciept_instance = TotalReciept.objects.create(**validate_data)
        for item_data in subprice_data_items:
            sub = Supreceipt.objects.create(total_reciet_fk=Reciept_instance, **item_data)
        
        return Reciept_instance
    

class ListHistorySerializer(serializers.ModelSerializer):
    restaurant_name = ResturantNameserializer(source='total_reciet_fk.res_fk') 

    class Meta:
        model = Supreceipt 
        fields = ['id', 'food_fk', 'size_fk', 'quantity', 'totalsupprice', 'restaurant_name']
       