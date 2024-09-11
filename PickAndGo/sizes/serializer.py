from rest_framework import serializers
from .models import Size


class sizeserializer(serializers.ModelSerializer):
    owner_fk = serializers.ReadOnlyField(source='owner_fk.username') 
    class Meta:
        model = Size
        fields = ['size', 'price', 'owner_fk']
        read_only_fields = ['owner_fk'] 