from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import foodviewset



# urlpatterns=[
#     path('createfood/',foodviewset.as_view(),name="food creation")
# ]
router=DefaultRouter()

router.register(r'food',foodviewset)

urlpatterns=[
    path('',include(router.urls))
]