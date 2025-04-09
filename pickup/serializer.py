from rest_framework import serializers
from .models import PickUp

class pickupserializer(serializers.ModelSerializer):
   

   
   class Meta:
        model=PickUp
        fields="__all__"