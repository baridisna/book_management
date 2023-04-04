from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import copy

from .forms import BookForm
from .models import Book


@login_required(login_url='/login/')
def BookView(request):
    user = request.user
    if user.role.slug == 'administrator':
        books = Book.objects.all()[:10]
    else:
        books = Book.objects.filter(created_by=user)

    navigation = {
        'second': 'Books'
    }
    return render(request=request, template_name="books.html", 
                  context={"navigation": navigation, "books": books, "user": user})


@login_required(login_url='/login/')
def BookAddView(request):    
    if request.method == 'POST':
        data = copy.copy(request.POST)
        data['created_by'] = request.user
        form = BookForm(data, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully.")
            return redirect("/books")
        else:
            messages.error(request, "Invalid Information.")
    else:
        form = BookForm()

    navigation = {
        'second': 'Books',
        'second_url': '/books/',
        'third': 'Add'
    }
    user = request.user
    return render(request=request, template_name="books-add.html", 
                  context={"navigation": navigation, "form": form, "user": user})


@login_required(login_url='/login/')
def BookEditView(request, id):
    book = Book.objects.get(pk=id)
    user = request.user

    # Validate member can only edit their book
    if request.user.role.slug == 'member' and book.created_by != user:
        return redirect('error/401')

    form = BookForm(request.POST or None, request.FILES or None, instance = book)
    if form.is_valid():
        form.save()
        messages.success(request, "Book data changed")
    else:
        messages.error(request, "Invalid Information")

    # navigation in title template nav-title.html
    navigation = {
        'second': 'Books',
        'second_url': '/books/',
        'third': 'Edit'
    }
    return render(request=request, template_name="books-edit.html",
        context={"form": form, "navigation": navigation, "user": user})


@login_required(login_url='/login/')
def BooksDestroyView(request, id):
    book = Book.objects.get(pk=id)
    user = request.user

    # Validate member can only edit their book
    if request.user.role.slug == 'member' and book.created_by != user:
        return redirect('error/401')

    book.delete()
    return redirect('/books/') 
