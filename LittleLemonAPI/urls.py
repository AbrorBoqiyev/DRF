from django.urls import path
from .views import *

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items', menu_items),
    path('menu-items/<int:pk>', single_item),  
    path('menu-items/category', Category_view),
    path('secret/', secret),  
    path('api-token-auth', obtain_auth_token),
    path('manager-view/', manager_view),
    path('throttle-check/', throttle_check),
    path('throttle-check-auth', throttle_check_auth),
]
