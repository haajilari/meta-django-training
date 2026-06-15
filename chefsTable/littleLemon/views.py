from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from littleLemon.forms import InputForm
# from .models import Menu
# Create your views here.

def hello(request):
    return HttpResponse("Hello, SAG!")

# # def menu_by_id(request, menu_id):
# #     menu


def say_hello(request):
    return HttpResponse("Hello, And You are a KHAR :)!")

def home(request):
    date_joined = datetime.now().today().strftime("%Y-%m-%d")
    return HttpResponse(f"Welcome to the KHAR STATION :) - Joined on {date_joined}")

def form_view(request):
    form = InputForm()
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "form.html", context)