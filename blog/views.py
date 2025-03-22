from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


def home(request):
    # select_related() -> fetches related authors in one query for efficiency:
    posts = Post.objects.select_related('author').all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_create(request):
    if not request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blog:home')
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})


def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/post_details.html', {'post': post})


def post_update(request, pk):
    if not request.user.is_authenticated:
        return redirect('blog:home')

    post = get_object_or_404(Post, id=pk)

    if request.user != post.author:
        return redirect('blog:home')

    form = PostForm(data=request.POST or None, instance=post)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('blog:post_details', pk=post.pk)

    return render(request, 'blog/blog_update.html', {'form': form})


def post_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('blog:home')

    post = get_object_or_404(Post, id=pk)

    if request.user != post.author:
        return redirect('blog:home')

    if request.method == 'POST':
        post.delete()
        next_url = request.GET.get('next', 'blog:home')
        return redirect(next_url)

    return render(request, 'blog/blog_delete.html', {'post': post})
