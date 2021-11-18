from rest_framework.serializers import ModelSerializer

from store.models import Author, Book


class AuthorsSerializer2(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'born', 'alias']


class BooksSerializer(ModelSerializer):
    author = AuthorsSerializer2()

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'pages_count']


class AuthorsSerializer(ModelSerializer):
    books = BooksSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'born', 'alias', 'books']
