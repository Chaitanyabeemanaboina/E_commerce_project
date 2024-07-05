from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=30)
    prize = models.FloatField()
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=30)
    bill = models.BooleanField(default=False)
    add_to_cart = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/',null=True)