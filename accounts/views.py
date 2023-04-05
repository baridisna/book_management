from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

from .forms import RegisterForm, ProfileForm, UsersForm
from .models import Role, User


# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        role = Role.objects.get(slug='member')
        form = RegisterForm(request.POST or None, initial={'role': role})
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/profile")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    else:
        form = RegisterForm()
    return render(
        request=request, template_name="registration/register.html",
        context={"form": form})


@login_required(login_url='/login/')
def ProfileView(request):
    user = request.user

    form = ProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "Profile Changed")
    else:
        messages.error(request, "Invalid Information")
    navigation = {
        'second': 'Profile'
    }
    return render(
        request=request, template_name="profile.html",
        context={"form": form, "user": user, "navigation": navigation})


def RolesView(request):
    return render(
        request=request, template_name="roles.html", context={"test": "test"})


@login_required(login_url='/login/')
def UsersView(request):
    if request.user.is_superuser:
        print('akaka')
    if request.user.role.slug != "administrator" and not request.user.is_superuser:
        return redirect('/error/401')

    navigation = {
        'second': 'Users'
    }
    user = request.user
    return render(request=request, template_name="users.html",
                  context={"navigation": navigation, "user": user})


@login_required(login_url='/login/')
def UsersDataListView(request):
    if request.user.role.slug != "administrator" and not request.user.is_superuser:
        return HttpResponse("User unauthorized", status=401)

    users = User.objects.all()
    data = []
    for user in users:
        row = [
            user.first_name + ' ' + user.last_name,
            user.username,
            user.email,
            user.phone_number,
            user.date_of_birth.strftime("%d/%m/%Y"),
            user.role.name,
            user.id
        ]
        data.append(row)
    return HttpResponse(json.dumps(data, default=str))


@login_required(login_url='/login/')
def UsersAddView(request):
    if request.user.role.slug != "administrator" and not request.user.is_superuser:
        return redirect('/error/401')

    if request.method == 'POST':
        form = UsersForm(request.POST)
        print("here already")
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully.")
            return redirect("/users")
        else:
            messages.error(request, "Invalid Information.")
    else:
        form = UsersForm()

    navigation = {
        'second': 'Users',
        'second_url': '/users/',
        'third': 'Add'
    }
    user = request.user
    return render(
        request=request, template_name="users-add.html",
        context={"navigation": navigation, "form": form, "user": user})


@login_required(login_url='/login/')
def UsersEditView(request, id):
    if request.user.role.slug != "administrator" and not request.user.is_superuser:
        return redirect('/error/401')

    user = User.objects.get(pk=id)
    form = UsersForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, "User data changed")
    else:
        messages.error(request, "Invalid Information")

    # navigation in title template nav-title.html
    navigation = {
        'second': 'Users',
        'second_url': '/users/',
        'third': 'Edit'
    }
    user = request.user
    return render(
        request=request, template_name="users-edit.html",
        context={"form": form, "navigation": navigation, "user": user})


@login_required(login_url='/login/')
def UsersDestroyView(request, id):
    if request.user.role.slug != "administrator" and not request.user.is_superuser:
        return redirect('/error/401')

    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/users/')
