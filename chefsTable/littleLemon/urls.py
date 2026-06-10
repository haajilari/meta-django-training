from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello,),
    path('say-hello/', views.say_hello, name='say_hello'),
    path('home/', views.home, name='home')
    # path('menu/<int:menu_id>/', views.menu_by_id, name='menu_by_id')
]