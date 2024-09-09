
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import resturantviewset



# urlpatterns=[
#     path('createresturant/',resturantviewset.as_view(), name='resturant-create')
router=DefaultRouter()

router.register(r'resturant',resturantviewset)

urlpatterns=[
    path('',include(router.urls))
]
