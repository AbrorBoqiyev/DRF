from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)