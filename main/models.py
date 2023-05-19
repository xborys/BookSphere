from django.db import models
from .choices import get_nationality_from_file, get_book_category_from_file

class author(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50, choices=get_nationality_from_file())
    birth = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.lastname


class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=get_book_category_from_file())
    publish_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.author.name + ' ' + self.author.lastname + ' | ' + self.title
    
class borrower(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.lastname

class books_loan(models.Model):
    borrower = models.ForeignKey(borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    start_loan = models.DateField(auto_now_add=True)
    end_loan = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.borrower.name + ' ' + self.borrower.lastname + ' | ' + str(self.book.author) + ' ' + self.book.title


