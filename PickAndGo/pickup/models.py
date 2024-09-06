from django.db import models
from users.models import CustomUser
from users.models import Owner

# Create your models here.
class PickUp(models.Model):
    user_fk=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='pickupsusername')
    owner_fk=models.ForeignKey(Owner,on_delete=models.CASCADE, related_name='pickupsowner')
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready'),
    ]

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    time=models.TimeField()
