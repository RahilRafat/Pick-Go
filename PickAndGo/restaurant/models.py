from django.db import models
# from users.models import Adminn

# Create your models here.

class Restaurant(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=13)
    address=models.TextField()
    img=models.ImageField( blank=True, null=True,upload_to='./media/')
    admin_fk=models.ForeignKey('users.CustomUser',on_delete=models.CASCADE,blank=True, null=True)


