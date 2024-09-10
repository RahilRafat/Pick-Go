from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import sizeviewset

router=DefaultRouter()
router.register(r'size',sizeviewset)

urlpatterns=[
    path('',include(router.urls))
]