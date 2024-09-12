from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import foodviewset

router=DefaultRouter()

router.register(r'food',foodviewset)

urlpatterns=[
    path('',include(router.urls))
]