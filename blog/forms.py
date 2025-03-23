from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'picture')

        labels = {
            'title': '',
            'content': '',
            'picture': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-4', 'placeholder': 'Description', 'style': 'resize:none;'}),
        }
