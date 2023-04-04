from django.urls import path

from .views import BookAddView, BookView, BookEditView, BooksDestroyView


urlpatterns = [
    path('', BookView, name='books'),
    path('add', BookAddView, name='books-add'),
    path('<int:id>/edit', BookEditView, name='books-edit'),
    path('<int:id>/delete', BooksDestroyView, name='books-delete'),
]
