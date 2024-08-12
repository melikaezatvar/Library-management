from django.urls import path
from .views import book_list, book_detail, book_create_update

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:book_id>', book_detail, name='book_detail'),
    path('create/', book_create_update, name='book_create_update'),
    path('edit/<int:book_id>', book_create_update, name='book_edit'),
]