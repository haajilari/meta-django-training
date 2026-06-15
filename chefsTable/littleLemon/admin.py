from django.contrib import admin

from .models import Menu, MenuCategory, InputForm,Reservation

# Register your models here.

admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(InputForm)
admin.site.register(Reservation)