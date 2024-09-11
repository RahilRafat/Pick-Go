from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import pickviews



# urlpatterns=[
#     path('createresturant/',resturantviewset.as_view(), name='resturant-create')
router=DefaultRouter()

router.register(r'pick',pickviews)

urlpatterns=[
    path('',include(router.urls))
]