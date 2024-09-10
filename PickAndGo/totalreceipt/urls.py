from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RecieptViewSet


router=DefaultRouter()
router.register(r'reciept',RecieptViewSet)

urlpatterns=[
    path('',include(router.urls))
]