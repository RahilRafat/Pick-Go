from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Supreceipt
from .serializer import SubPriceSerializer
class SubPriceViewSet(viewsets.ModelViewSet):
   
    queryset=Supreceipt.objects.all()
    serializer_class=SubPriceSerializer
    def create(self , request):
        subserializer=SubPriceSerializer (data =self.request.data)
        subserializer.is_valid()
        subserializer.save()
        return Response(subserializer.data)