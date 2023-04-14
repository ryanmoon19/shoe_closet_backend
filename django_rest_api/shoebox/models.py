from django.db import models

# Create your models here.
class Shoes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.TextField()