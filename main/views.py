from django.shortcuts import render
from .models import book, author, borrower, books_loan
from .forms import AuthorForm, BookForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, 'index.html', {})

def books(request):
    books = book.objects.all()

    return render(request, 'books.html',
                  {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = BookForm()

    return render(request, 'add_book.html',
                  {'form' : form})

def authors(request):
    authors = author.objects.all()

    return render(request, 'authors.html',
                  {'authors' : authors})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()

    return render(request, 'add_author.html',
                  {'form': form})


def borrowers(request):
    borrowers = borrower.objects.all()

    return render(request, 'borrowers.html',
                  {'borrowers' : borrowers})

def book_loan(request):
    book_loan = books_loan.objects.all()

    return render(request, 'books_loan.html',
                  {'books_loan' : book_loan})
