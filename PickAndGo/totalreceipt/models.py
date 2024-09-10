from django.db import models
# from supreceipt.models import Supreceipt
from users.models import CustomUser
from restaurant.models import Restaurant

# Create your models here.
class TotalReciept(models.Model):
    # subprice_fk=models.ForeignKey(Supreceipt,on_delete=models.CASCADE)
    user_fk=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total_receipt=models.IntegerField(blank = True ,null=True)
    n_order=models.IntegerField(default=1)
    res_fk=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
