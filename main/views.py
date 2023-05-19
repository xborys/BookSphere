from django.shortcuts import render
from .models import book, author, borrower, books_loan

def index(request):
    return render(request, 'index.html', {})

def books(request):
    books = book.objects.all()

    return render(request, 'books.html',
                  {'books': books})

def authors(request):
    authors = author.objects.all()

    return render(request, 'authors.html',
                  {'authors' : authors})

def borrowers(request):
    borrowers = borrower.objects.all()

    return render(request, 'borrowers.html',
                  {'borrowers' : borrowers})

def book_loan(request):
    book_loan = books_loan.objects.all()

    return render(request, 'books_loan.html',
                  {'books_loan' : book_loan})
