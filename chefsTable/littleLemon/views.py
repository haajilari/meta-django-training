from django.shortcuts import render
from django.http import HttpResponse
# from .models import Menu
# Create your views here.

def hello(request):
    return HttpResponse("Hello, SAG!")

# def menu_by_id(request, menu_id):
#     menu