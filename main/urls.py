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
    path('borrower/add_borrower/', views.add_borrower, name='add-borrower'),
    path('books_loan/', views.book_loan, name='books_loan'),
    path('books_loan/add_book_loan/', views.add_book_loan, name='add-book-loan'),
]
