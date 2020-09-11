import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def user_auth(request):
    return HttpResponse('Login works fine.')
