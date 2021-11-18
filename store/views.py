from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from store.api.serializers import AuthorsSerializer, BooksSerializer
from store.models import Author, Book


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.prefetch_related('books').all()
    serializer_class = AuthorsSerializer


class BooksViewSet(ModelViewSet):
    # queryset = Book.objects.select_related('author').all()
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

    # @method_decorator(vary_on_cookie) # для каждого пользователя отдельное кэширование
    @method_decorator(cache_page(20 * 1))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@cache_page(60 * 2)
def books_list(request):
    books = Book.objects.all()
    context = {
        'books': books,
        'title': 'Books list',
    }
    return render(request, 'store/books_list.html', context=context)
