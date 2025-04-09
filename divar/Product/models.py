from django.db import models
from User.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 20)
    price = models.PositiveBigIntegerField()
    seller = models.ForeignKey(to=User, on_delete = models.CASCADE)
    is_sold = models.BooleanField(default=False)