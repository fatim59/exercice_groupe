from django.contrib import admin
from . models import *

@admin.register(Ingredient) 
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'date_upd', 'statut')       

    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'name_plat', 'prix', 'date_add', 'date_upd', 'image','statut')
    
@admin.register(Dishes) 
class DishesAdmin(admin.ModelAdmin):
    list_display = ('title', 'name_plat', 'description', 'image', 'prix', 'date_add', 'date_upd', 'statut', 'numero')  
    
    
@admin.register(Job) 
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_add', 'date_upd', 'statut')
    
@admin.register(Chef) 
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'date_add', 'date_upd', 'statut')    
    
@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'date_add', 'date_upd', 'statut' )

# Register your models here.
