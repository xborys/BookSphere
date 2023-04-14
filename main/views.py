from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html', {})

def books(request):
    books = book.objects.all()

    return render(request, 'books.html',
                  {'books': books})