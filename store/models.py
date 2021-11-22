from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    born = models.DateField(blank=True, null=True)
    alias = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True)
    pages_count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
