from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import SizeViewSet

router=DefaultRouter()
router.register(r'size',SizeViewSet)

urlpatterns=[
    path('',include(router.urls))
]