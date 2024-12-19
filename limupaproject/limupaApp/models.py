from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField(null=True)

    def is_in_stock(self):
        if self.stock is None:
            return False
        return self.stock > 0
    is_in_stock.boolean = True



    def __str__(self):
        return self.name

