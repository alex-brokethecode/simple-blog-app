from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mb-4',
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control mb-4',
                'placeholder': 'Password',
            }
        )
    )
