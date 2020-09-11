import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            context = {'form': form}

            # return render(request, "users/login.html", context)
            return redirect('login')

    if request.method == "GET":
        form = RegisterForm()

        context = {'form': form}

        return render(request, "users/register.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user_auth/')

        else:
            return HttpResponse('Invalid login.')

    if request.method == "GET":
        form = LoginForm()

        return render(request, "users/login.html", {"form": form})


def user_auth(request):
    if request.user.is_authenticated():
        if request.method == "GET":
            first_name = request.user.first_name()
            last_name = request.user.last_name()

            context = {"first_name": first_name,
                       "last_name": last_name
                       }

            return render(request, 'users/auth.html', context)
    else:
        return HttpResponse('User is not authenticated.')
