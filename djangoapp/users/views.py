import json

import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to login')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def user_auth(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email

    context = {'first_name': first_name,
               'last_name': last_name,
               'email': email}

    # FastAPI
    # url = 'http://localhost:8000/check'

    # Flask
    url = 'http://localhost:4000/check'

    fastapi_response = requests.post(url, json=context)

    response = {
        'response': fastapi_response.text
    }

    resp = response['response']
    if resp == 'PASS':
        return HttpResponse('User is in the database.')
    else:
        return HttpResponse('User is not in the database.')
