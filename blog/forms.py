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
            'title': forms.TextInput(attrs={'class': 'form-control mt-4 mb-2', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control mt-4 mb-3', 'placeholder': 'Description', 'style': 'resize:none;'}),
        }
