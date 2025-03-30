from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserLoginForm, UserRegisterForm


def user_login(request):
    next_url = request.GET.get('next', 'blog:home')

    if request.user.is_authenticated:
        return redirect(next_url)

    form = UserLoginForm(data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect(next_url)
        else:
            form.add_error(None, 'Invalid username or password')

    return render(request, 'users/user_login.html', {'form': form})


def user_register(request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('blog:home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/user_register.html', {'form': form})


@login_required(login_url='users:user_login')
def user_logout(request):
    next_url = request.GET.get('next', 'blog:home')
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect(next_url)
