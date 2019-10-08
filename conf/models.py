from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    
class Recipe(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
# Create your models here.

class Change(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut =  models.BooleanField(default=True) 
    
class Dishes(models.Model):
    name_plat = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)  
    statut =  models.BooleanField(default=True) 
      
    
    
