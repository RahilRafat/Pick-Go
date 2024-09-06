from django.db import models
from supreceipt.models import Supreceipt
from users.models import CustomUser

# Create your models here.
class TotalReciept(models.Model):
    subprice_fk=models.ForeignKey(Supreceipt,on_delete=models.CASCADE)
    user_fk=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total_receipt=models.DecimalField(decimal_places=2,max_digits=7)
    
