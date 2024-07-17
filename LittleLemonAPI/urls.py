from django.urls import path
from .views import *

urlpatterns = [
    path('menu-items', MenuItemsView.as_view()),
]
