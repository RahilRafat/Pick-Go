from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import SubPriceViewSet

router=DefaultRouter()
router.register(r'subprice',SubPriceViewSet)

urlpatterns=[
    path('',include(router.urls))
]