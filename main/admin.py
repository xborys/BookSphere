from django.contrib import admin
from .models import *

admin.site.register(book)
admin.site.register(author)
admin.site.register(borrower)
admin.site.register(books_loan)