from django.contrib import admin

from .models import Menu, MenuCategory, InputForm

# Register your models here.

admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(InputForm)