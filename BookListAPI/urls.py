from django.urls import path
from .views import *

urlpatterns = [
    path('', bookview),
    # path('books/', books)
    path('books/', BookList.as_view()),
    path('books/<int:pk>', Book.as_view()),
]
