from django.http import HttpResponse
from django.shortcuts import render


def test_form(request):
    if request.method == "POST":
        user = request.POST.get('username')
        user.save()
        if user == "mark":
            return HttpResponse('hello mark')
        else:
            return HttpResponse(f'Hello {user}!')

    return render(request, 'form.html')
