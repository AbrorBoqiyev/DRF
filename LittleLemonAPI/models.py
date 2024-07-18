from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

class Category(models.Model):
    slug = models.CharField(max_length=150)
    title = models.CharField(max_length=150)