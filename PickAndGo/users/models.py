from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from restaurant.models import Restaurant
# from django.contrib.auth.hashers import make_password
# from totalreceipt.models import TotalReciept

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, phone, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner=models.BooleanField(default=False)
  
    objects = CustomUserManager()  

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']

   


    class Meta:
        permissions = [
            ("can_view_customuser", "Can view CustomUser"),
            ("can_create_owner", "Can create owner"),
        ]

    

        
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )
    




# class Admin(CustomUser):
#     # is_admin=models.BooleanField(default=True)
#     pass



# class Owner(CustomUser):
   
#     admin_fk=models.ForeignKey('users.Admin',on_delete=models.CASCADE,null=False)
#     res_fk=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    




