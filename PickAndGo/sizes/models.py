from django.db import models
from restaurant.models import Restaurant
from users.models import CustomUser
from food.models import Food

# Create your models here.
class Size(models.Model):
    size=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    food_fk=models.ForeignKey(Food,on_delete=models.CASCADE)
    owner_fk=models.ForeignKey(CustomUser,on_delete=models.CASCADE)



