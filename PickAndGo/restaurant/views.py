from rest_framework import viewsets, permissions
from .models import Restaurant
from .serializers import RestaurantSerializer
from .permissions import IsAdminUser,IsOwnerUser,IsCustomUser
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
    serializer_class = RestaurantSerializer
    permission_classes=[IsAuthenticated,(IsAdminUser|IsOwnerUser|IsCustomUser)]
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_class=RestaurantFilter
    search_fields=['name']



    def perform_create(self, serializer):
        """
        Override perform_create to include custom logic when creating a Restaurant instance.
        """
        user = self.request.user
        
        # Log user details for debugging
        # print(f"User: {user.username}, User ID: {user.id}, User Type: {'Admin' if user.is_staff else 'Regular User'}")
        # print(f"Request Method: {self.request.method}")
        # print(f"Request Data: {self.request.data}")

        # Save the new instance with the current user as admin_fk
        serializer.save(admin_fk=user)





    def perform_update(self, serializer):
        user = self.request.user
        restaurant = self.get_object()
        
        # Check if the user is the owner or admin
        if user != restaurant.owner_fk or not user.is_staff:
            raise PermissionDenied("You do not have permission to update this restaurant.")
        
        serializer.save()


    def perform_update(self, serializer):
        """
        Override perform_create to include custom logic when creating a Restaurant instance.
        """
        user = self.request.user
        
        # # Log user details for debugging
        # print(f"User: {user.username}, User ID: {user.id}, User Type: {'owner' if user.is_owner else 'Regular User'}")
        # print(f"Request Method: {self.request.method}")
        # print(f"Request Data: {self.request.data}")

        # # Save the new instance with the current user as admin_fk
        serializer.save(owner_fk=user)





    def perform_destroy(self, instance):
        user = self.request.user
        
        # Check if the user is the owner or admin
        if user != instance.owner_fk or not user.is_staff:
            raise PermissionDenied("You do not have permission to delete this restaurant.")
        
        instance.delete()
