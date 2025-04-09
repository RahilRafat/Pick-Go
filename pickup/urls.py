from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import pickviews


router=DefaultRouter()

router.register(r'pick',pickviews)

urlpatterns=[
    path('',include(router.urls))
]