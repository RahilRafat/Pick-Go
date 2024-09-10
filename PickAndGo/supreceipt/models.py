from django.db import models
from food.models import Food
from sizes.models import Size
from users.models import CustomUser
from totalreceipt.models import TotalReciept

# Create your models here.
class Supreceipt(models.Model):
    food_fk=models.ForeignKey(Food, on_delete=models.CASCADE)
    size_fk=models.ForeignKey(Size,on_delete=models.CASCADE)
    quantity =models.IntegerField()
    totalsupprice=models.IntegerField(null=True)
    total_reciet_fk=models.ForeignKey(TotalReciept,on_delete=models.CASCADE,default=1,blank= True, null= True)



