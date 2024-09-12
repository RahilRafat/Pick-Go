from django.shortcuts import render
from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import Food
from .serializer import foodserializer
from rest_framework.views import APIView
from .permissions import IsOwnerUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets,status
from rest_framework.response import Response

class foodviewset(viewsets.ModelViewSet):
    queryset=Food.objects.all()
    serializer_class=foodserializer
    permission_classes = [IsAuthenticated,IsOwnerUser]

    
