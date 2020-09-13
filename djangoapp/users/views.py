import json

import requests
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
    firstname = request.user.first_name
    lastname = request.user.last_name
    email = request.user.email

    context = {'firstname': firstname,
               'lastname': lastname,
               'email': email}

    context_json = json.dumps(context)
    url = 'http://localhost:8000/check/'

    x = requests.post(url, json=context_json)
    print(f'Response: {x}.')
    print(f'Text: {x.text}.')

    response = {
        'response': x.text
    }

    return JsonResponse(response, safe=False)

