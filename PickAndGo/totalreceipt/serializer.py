from rest_framework import serializers
from .models import TotalReciept
from supreceipt.models import Supreceipt
from supreceipt.serializer import SubPriceSerializer


class RecieptSerializer(serializers.ModelSerializer):
    subprice_data = SubPriceSerializer(many=True, required=False)

    class Meta:
        model=TotalReciept
        fields="__all__"
    def create(self,validate_data):
        subprice_data_items=validate_data.pop('subprice_data',[])
        Reciept_instance=Supreceipt.objects.create(**validate_data)
        SubPrice_fk=validate_data.get('subprice_fk')
        user_object=validate_data('user_fk')
        subprice_total=SubPrice_fk.totalsupprice
        
        for data in subprice_data_items:
            # data.pop('Reciept_instance',None)
            data_user_fk=data.get('user_object')
            if data_user_fk !=user_object:
                 raise serializers.ValidationError("Sub-orders must belong to the same user.")
            Reciept_instance.totalPrice=subprice_total*Reciept_instance.n_order
            #   order_count += 1
            # Reciept_instance.save()
            return Reciept_instance