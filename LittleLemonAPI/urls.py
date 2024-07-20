from django.urls import path
from .views import *

urlpatterns = [
    path('menu-items', menu_items),
    path('menu-items/<int:pk>', single_item),  
    path('menu-items/category', Category_view)  
]
