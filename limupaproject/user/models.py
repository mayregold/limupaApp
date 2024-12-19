from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=6, choices=[('buyer','Buyer'),('seller','Seller')])
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    location = models.CharField(max_length=100, blank=True)
   
    def __str__(self):
        return self.user.username