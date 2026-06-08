from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, PostForm
from .models import Post


def register(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect('login')

    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )


def user_login(request):

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                'feed'
            )

        else:

            messages.error(
                request,
                "Invalid username or password"
            )

    return render(
        request,
        'login.html'
    )


def user_logout(request):

    logout(request)

    return redirect(
        'login'
    )


@login_required(login_url='login')
def delete_account(request):

    user = request.user

    logout(request)

    user.delete()

    return redirect(
        'register'
    )


@login_required(login_url='login')
def feed(request):

    if request.method == "POST":

        form = PostForm(
            request.POST
        )

        if form.is_valid():

            post = form.save(
                commit=False
            )

            post.user = request.user

            post.save()

            return redirect(
                'feed'
            )

    posts = Post.objects.filter(
        user=request.user
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        'feed.html',
        {
            'form': PostForm(),
            'posts': posts
        }
    )