from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Post
from .forms import PostForm


def home(request):
    # Get request.GET.q query
    q = request.GET.get('q', '').strip()

    # select_related() -> fetches related authors in one query for efficiency:
    posts = Post.objects.select_related('author').filter(
        Q(title__icontains=q) | Q(content__icontains=q) if q else Q())

    return render(request, 'blog/home.html', {'posts': posts, 'q': q})


@login_required(login_url='users:user_login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully')

            return redirect('blog:home')
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})


def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/post_details.html', {'post': post})


@login_required(login_url='users:user_login')
def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.user != post.author:
        return redirect('blog:home')

    form = PostForm(data=request.POST or None,
                    files=request.FILES or None,
                    instance=post)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Post updated successfully')

        return redirect('blog:post_details', pk=post.pk)

    return render(request, 'blog/post_update.html', {'form': form, 'post_id': post.pk})


@login_required(login_url='users:user_login')
def post_delete(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.user != post.author:
        return redirect('blog:home')

    if request.method == 'POST':
        post.delete()
        next_url = request.GET.get('next', 'blog:home')
        messages.success(request, 'Post deleted successfully')

        return redirect(next_url)

    return render(request, 'blog/post_delete.html', {'post': post})
