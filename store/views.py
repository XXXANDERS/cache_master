from django.core.cache import cache
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
        # a = 1 / 0
        return super().list(request, *args, **kwargs)


# @cache_page(60 * 2)
def books_list(request):
    # if cache.get('books', 'undefined') == 'undefined':
    #     books = Book.objects.select_related('author')
    #     cache.set('books', books, 40)

    # cache.add('books_count', Book.objects.count(), 40)
    # books_count = cache.get('books_count')
    # books_count = cache.get_or_set('books_count', Book.objects.count, 40)

    # r = cache.add('books', Book.objects.select_related('author'), 10)
    # print(r)
    # books = cache.get('books')
    books = cache.get_or_set('books', Book.objects.select_related('author'), 10)
    # cache.touch('books', 50)

    context = {
        'books': books,
        # 'books_count': books_count,
        'books_count_1': cache.get_or_set('books_count', Book.objects.count, 10, version=1),
        'books_count_2': cache.get_or_set('books_count', Book.objects.count, 60, version=2),
        'title': 'Books list',
    }
    return render(request, 'store/books_list.html', context=context)
