from django_filters import rest_framework as filters
from .models import Restaurant

class RestaurantFilter(filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = {
            'name': ['exact', 'icontains'], 
        }
