from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_create(request):
    return render(request, 'blog/post_create.html')


def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/post_details.html', {'post': post})


def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/blog_update.html', {'post': post})


def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/blog_delete.html', {'post': post})
