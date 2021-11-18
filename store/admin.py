from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Author, Book


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
