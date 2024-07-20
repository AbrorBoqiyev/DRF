from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal


# class MenuItemSerializer(serializers.Serializer):
#     id =  serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     inventory = serializers.IntegerField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    calculate_after_tax = serializers.SerializerMethodField(method_name='calcualte_tax')
    category = CategorySerializer(read_only=True)
    
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'calculate_after_tax', 'category']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

    def calcualte_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
    
        