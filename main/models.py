from django.db import models

class book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publish_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.author + ' ' + self.title