from django.shortcuts import render
from rest_framework import viewsets
from .models import Supreceipt

# Create your views here.
from .models import Supreceipt
from .serializer import SubPriceSerializer
class SubPriceViewSet(viewsets.ModelViewSet):
    # authentication_classes = []
    queryset=Supreceipt.objects.all()
    serializer_class=SubPriceSerializer
