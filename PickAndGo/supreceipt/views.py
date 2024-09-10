from django.shortcuts import render
from rest_framework import viewsets
from .models import Supreceipt
from rest_framework.response import Response
# Create your views here.
from .models import Supreceipt
from .serializer import SubPriceSerializer
class SubPriceViewSet(viewsets.ModelViewSet):
    # authentication_classes = []
    queryset=Supreceipt.objects.all()
    serializer_class=SubPriceSerializer
    def create(self , request):
        subserializer=SubPriceSerializer (data =self.request.data)
        subserializer.is_valid()
        subserializer.save()
        return Response(subserializer.data)