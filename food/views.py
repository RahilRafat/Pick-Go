from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Food
from .serializer import FoodSerializer
from rest_framework.views import APIView
from .permissions import IsFoodOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from restaurant.models import Restaurant
from rest_framework.exceptions import ValidationError

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated, IsFoodOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        res_fk = self.request.query_params.get('res_fk', None)
        if res_fk is not None:
            queryset = queryset.filter(res_fk=res_fk) 
        return queryset


    def perform_create(self, serializer):
      
        user = self.request.user
        restaurant_id = self.request.data.get('res_fk')

        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise PermissionDenied("Invalid restaurant ID.")

        if restaurant.owner_fk != user and not user.is_staff:
            raise PermissionDenied("You do not have permission to add food to this restaurant.")


        img = self.request.FILES.get('img')
        if not img:
            raise ValidationError({"img": "No image file was provided."})




        serializer.save()

    def perform_update(self, serializer):
        user = self.request.user
        food = self.get_object()
       
        if food.res_fk.owner_fk != user and not user.is_staff:
            raise PermissionDenied("You do not have permission to update this food item.")
        
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.res_fk.owner_fk != user and not user.is_staff:
            raise PermissionDenied("You do not have permission to delete this food item.")
        instance.delete()
