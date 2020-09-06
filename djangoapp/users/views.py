from django.http import HttpResponse
from django.shortcuts import render

def test_form(request):
    if request.method == "POST":
        user = request.POST.get('username')
        if user == "mark":
            return HttpResponse('hello mark')

    return render(request, "form.html")