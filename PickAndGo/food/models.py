from django.db import models
from restaurant.models import Restaurant 

# Create your models here.
class Food (models.Model):
     name=models.CharField(max_length=60)
     description=models.TextField()
     res_fk=models.ForeignKey(Restaurant,on_delete=models.CASCADE)


     class Meta:
        ordering = ['name']


