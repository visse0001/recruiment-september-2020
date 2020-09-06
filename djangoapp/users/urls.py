from django.urls import path

from .views import test_form

urlpatterns = [
    path('form/', test_form, name="form")
]
