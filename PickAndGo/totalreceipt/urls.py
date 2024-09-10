from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RecieptViewSet,UserOrderListView


router=DefaultRouter()
router.register(r'reciept',RecieptViewSet)

urlpatterns=[
    path('',include(router.urls)),


    path('user/orders/', UserOrderListView.as_view(), name='user-orders-list'),
]