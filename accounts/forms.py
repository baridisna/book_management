from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Role


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True)
    phone_number = forms.CharField(required=True)
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=False)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'date_of_birth',
            'phone_number', 'password1', 'password2', 'role'
        )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'date_of_birth',
            'phone_number')


class UsersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)

        self.fields['role'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        return "%s" % obj.name

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'date_of_birth',
            'phone_number', 'role')
