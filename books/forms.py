from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'title', 'slug', 'description', 'author', 'cover', 'created_by']
