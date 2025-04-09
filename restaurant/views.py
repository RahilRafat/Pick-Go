from rest_framework import viewsets, permissions
from .models import Restaurant
from restaurant.serializer import ResturantSerializer
from .permissions import IsAdminUser,IsOwnerOrReadOnly
from users.models import CustomUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .filters import RestaurantFilter

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = ResturantSerializer
    permission_classes=[IsAuthenticated,IsOwnerOrReadOnly]
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_class=RestaurantFilter
    search_fields=['name']


    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_staff:
            raise PermissionDenied("Only staff members can create a restaurant.")
        owner_id = self.request.data.get('owner_fk')
        if owner_id:
            try:
                owner = CustomUser.objects.get(pk=owner_id, is_owner=True)
                serializer.save(admin_fk=user, owner_fk=owner)
            except CustomUser.DoesNotExist:
                raise PermissionDenied("Invalid owner ID or the user is not an owner.")
        else:
            serializer.save(admin_fk=user)


    def perform_update(self, serializer):
        user = self.request.user
        restaurant = self.get_object()
        
        if user != restaurant.owner_fk and not user.is_staff:
            raise PermissionDenied("You do not have permission to update this restaurant.")
        
        serializer.save()

 
    def perform_destroy(self, instance):
        user = self.request.user
        
        
        if user != instance.owner_fk and not user.is_staff:
            raise PermissionDenied("You do not have permission to delete this restaurant.")
        
        instance.delete()
