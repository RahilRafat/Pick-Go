from django.db import models
from users.models import CustomUser
from restaurant.models import Restaurant

class TotalReciept(models.Model):
   
    user_fk=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total_receipt=models.IntegerField(blank = True ,null=True)
    n_order=models.IntegerField(default=1)
    res_fk=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    datte=models.DateField(default="2024-9-11")
