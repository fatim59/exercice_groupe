from django.contrib import admin
from . models import *

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image','date_add', 'date_upd', 'statut')
    
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('description', 'image','date_add', 'date_upd', 'statut')   
    
@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'date_add', 'date_upd', 'statut' ) 
    
@admin.register(Dishes) 
class DishesAdmin(admin.ModelAdmin):
    list_display = ('name_plat', 'date_add', 'date_upd', 'statut' )    

# Register your models here.
