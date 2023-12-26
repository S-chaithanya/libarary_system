# library/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:author_name>/', views.search_books, name='search_books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('take_book/<int:book_id>/', views.take_book, name='take_book'),
    path('return_book/<int:transaction_id>/', views.return_book, name='return_book'),
]
