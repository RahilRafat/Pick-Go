from django.db import models
from users.models import CustomUser


# Create your models here.
class PickUp(models.Model):
    user_fk=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='pickupsusername')
    owner_fk=models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='pickupsowner')
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready'),
        ('confirmed', 'confirmed'),
    ]

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    time=models.DateTimeField(null=True,blank=True)

    confirmation=models.BooleanField(default=False)
