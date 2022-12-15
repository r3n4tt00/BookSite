from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('searched_books', views.search_book, name = 'book_search'),
]
