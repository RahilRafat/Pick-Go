
from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet



# urlpatterns=[
#     path('createresturant/',resturantviewset.as_view(), name='resturant-create')
router=DefaultRouter()

router.register(r'resturant',RestaurantViewSet)

urlpatterns=[
    path('',include(router.urls))
]
