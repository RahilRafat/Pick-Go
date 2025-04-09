from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import RecieptViewSet,UserOrderListView
from .views import UserOrderHistoryView


router=DefaultRouter()
router.register(r'reciept',RecieptViewSet)

urlpatterns=[
    path('',include(router.urls)),


    path('user/orders/', UserOrderListView.as_view(), name='user-orders-list'),
    path('api/order-history/', UserOrderHistoryView.as_view(), name='user_order_history'),

]