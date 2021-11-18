from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    born = models.DateField()
    alias = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    pages_count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
