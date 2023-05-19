from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    path('borrower/', views.borrowers, name='borrowers'),
    path('books_loan/', views.book_loan, name='books_loan'),
]
