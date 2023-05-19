from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('books/add_book/', views.add_book, name='add-book'),
    path('authors/', views.authors, name='authors'),
    path('authors/add_author/', views.add_author, name='add-author'),
    path('borrower/', views.borrowers, name='borrowers'),
    path('books_loan/', views.book_loan, name='books_loan'),
]
