from django.db import models

# Create your models here.

# Menu Category
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=255)

class Menu(models.Model):
    menu_item= models.CharField(max_length=255)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT,default=None)
                                    

class InputForm(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

class Reservation(models.Model):
    name = models.CharField(max_length=255,blank=True)
    contact = models.CharField("Phone Number",max_length=255,blank=True)
    time = models.TimeField()
    count=models.IntegerField()
    notes = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.name