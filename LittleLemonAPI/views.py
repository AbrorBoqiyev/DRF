from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, pk):
    item = get_object_or_404(MenuItem,id=pk)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)






@api_view(['GET','POST'])
def Category_view(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        St_Category = CategorySerializer(queryset, many=True)
        return Response(St_Category.data)
    if request.method == 'POST':
        Sd_Category = CategorySerializer(data=request.data)
        Sd_Category.is_valid(raise_exception=True)
        Sd_Category.save()
        return Response(Sd_Category.data, status.HTTP_201_CREATED)
    
