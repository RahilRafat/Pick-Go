from rest_framework import serializers
from .models import Size


class sizeserializer(serializers.ModelSerializer):
    owner_fk = serializers.ReadOnlyField(source='owner_fk.id') 
    class Meta:
        model = Size
        fields = ['id','size', 'price', 'food_fk','owner_fk']
        read_only_fields = ['owner_fk'] 
        