from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Size
from sizes.serializer import sizeserializer
from rest_framework.response import Response

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = sizeserializer
    filterset_fields = ('food_fk',)

    # @action(detail=False, methods=['get'], url_path='sizes_per_food/(?P<food_id>\d+)')
    # def sizes_per_food(self, request, food_id=None):
    #     """
    #     Custom action to get all sizes related to a specific food_id.
    #     """
    #     sizes = self.queryset.filter(food_fk_id=food_id)
    #     serializer = self.get_serializer(sizes, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, food_fk=None):
     
        food_fk = self.request.query_params.get('food_fk')
        
        if food_fk is None:
            return Response({'detail': 'food_id is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Filter sizes based on `food_id`
        self.queryset = self.queryset.filter(food_fk_id=food_fk)
        sizes = self.get_queryset()
        
        if not sizes:
            return Response({'detail': 'No sizes found for this food.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(sizes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

















    def get_queryset(self):
        """
        Override the default `get_queryset` method to filter sizes based on the
        owner and the food item if provided.
        """ 
        user = self.request.user
        queryset = super().get_queryset().filter(owner_fk=user)
        return queryset

    @action(detail=False, methods=['get'], url_path='sizes_per_food/(?P<food_id>\d+)')
    def sizes_per_food(self, request, food_id=None):
        user = request.user
        
        # Filter sizes based on the authenticated user and food_id
        sizes = self.queryset.filter(food_fk_id=food_id, owner_fk=user)
        serializer = self.get_serializer(sizes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        # Automatically set the owner_fk field to the current user
        serializer.save(owner_fk=self.request.user)

    def perform_update(self, serializer):
        # Ensure that owner_fk is not changed by the client
        serializer.save(owner_fk=self.request.user)
