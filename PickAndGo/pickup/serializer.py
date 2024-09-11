from rest_framework import serializers
from .models import PickUp

class pickupserializer(serializers.ModelSerializer):
   # time = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')

   
   class Meta:
        model=PickUp
        fields="__all__"