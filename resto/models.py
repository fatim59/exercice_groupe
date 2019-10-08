from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=250)
    name_plat = models.CharField(max_length=250)
    prix = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='picture')
    statut = models.BooleanField(default=True)
    ingredient_id = models.ForeignKey(Ingredient, on_delete= models.CASCADE, related_name='Ingredient_menu')
    
    def __str__(self):
        return self.title

class Dishes(models.Model):
    title = models.CharField(max_length=250)
    name_plat = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    prix = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    numero = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Job(models.Model):
    name = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Chef(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True) 
    Job_id = models.ForeignKey(Job, on_delete= models.CASCADE, related_name='Job_chef')
    
    
    def __str__(self):
        return self.name
    

class Change(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut =  models.BooleanField(default=True) 