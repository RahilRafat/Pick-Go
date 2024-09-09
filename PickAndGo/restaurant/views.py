from rest_framework import viewsets, permissions
from .models import Restaurant
from .serializers import RestaurantSerializer
from .permissions import IsAdminUser
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Restaurant
from .serializer import resturantserializer
from rest_framework.views import APIView
# from .permissions import IsAdminUser


# Create your views here.
from rest_framework import viewsets

class resturantviewset(viewsets.ModelViewSet):
    queryset=Restaurant.objects.all()
    serializer_class=resturantserializer
    # permission_classes = [ IsAdminUser]

    def perform_create(self, serializer):
        # Optionally, you can add extra logic here
        serializer.save()
