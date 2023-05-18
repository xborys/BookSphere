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