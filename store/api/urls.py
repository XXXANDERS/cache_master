from django.urls import path
from rest_framework.routers import DefaultRouter
from store.views import AuthorsViewSet, BooksViewSet, books_list

router = DefaultRouter()
router.register(r'authors', AuthorsViewSet)
router.register(r'books', BooksViewSet)
urlpatterns = [
    path('books-list/', books_list)
]
urlpatterns += router.urls
