from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# TODO: Use built-in AuthenticationForm or modify this to create a user profile


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mt-4',
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2 mt-4',
                'placeholder': 'Password',
            }
        )
    )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-2 mt-4',
                'placeholder': 'Username',
            }
        )
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2 mt-4',
                'placeholder': 'Password',
            }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-2 mt-4',
                'placeholder': 'Password confirmation',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
