from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Size
from .serializer import sizeserializer
from rest_framework.decorators import action

# Create your views here.
from rest_framework import viewsets

class sizeviewset(viewsets.ModelViewSet):
    queryset=Size.objects.all()
    serializer_class=sizeserializer


    @action(detail=False, methods=['get'], url_path='sizes_per_food/(?P<food_id>\d+)')
    def sizes_per_food(self,request,food_id=None):
        sizes=self.queryset.filter(food_id=food_id)
        serializer = self.get_serializer(sizes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
