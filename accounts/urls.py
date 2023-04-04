from django.contrib.auth import views
from django.urls import path
from django.views.generic import TemplateView

from .views import (
    ProfileView,
    RegisterView,
    RolesView,
    UsersAddView,
    UsersDataListView,
    UsersView,
    UsersDestroyView,
    UsersEditView)


urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView, name='profile'),
    path('users/', UsersView, name='users'),
    path('users/data', UsersDataListView, name='users-data'),
    path('users/add', UsersAddView, name='users-add'),
    path('users/<int:id>/edit', UsersEditView, name='users-edit'),
    path('users/<int:id>/delete', UsersDestroyView, name='users-edit'),
    path('roles/', RolesView, name='roles'),

    # error page
    path('error/401',
         TemplateView.as_view(template_name="errors/401.html"),
         name='err401'),
    path('error/404',
         TemplateView.as_view(template_name="errors/404.html"),
         name='err404'),
    path('error/500',
         TemplateView.as_view(template_name="errors/500.html"),
         name='err500'),
]
