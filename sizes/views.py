from rest_framework import viewsets, permissions
from .models import Size
from .serializer import sizeserializer
from .permissions import IsSizeOwner  # Assuming you want to restrict access

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = sizeserializer
    permission_classes = [permissions.IsAuthenticated, IsSizeOwner]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        food_fk = self.request.query_params.get('food_fk', None)
        if food_fk is not None:
            queryset = queryset.filter(food_fk=food_fk)  # Filter by food_fk if it's provided
        return queryset





    def perform_create(self, serializer):
        serializer.save(owner_fk=self.request.user)  # Automatically assign the current user as owner

# You can add custom permission logic in the IsSizeOwner class, similar to your IsFoodOwner
