# exercice_groupe
les modeles resto

  # jai fais une table ingredient car different plat peu avoir plusiieurs ingredient (page menu)
class Ingredient(models.Model):

    name = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
   

# pour les differents menu et on pourra selectionner les differents ingredients(page menu)
class Menu(models.Models

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
        
#la class dishes pour la page single_dishes
class Dishes(models.Model

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
        
    #class job pour avoir la liste de tous les jobs du resto (page team)
class Job(models.Model):

    name = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
 
 #class chef il soccupe de l'image et a la cle de la table job qui affiche sur la page team
class Chef(models.Model):

    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True) 
    Job_id = models.ForeignKey(Job, on_delete= models.CASCADE, related_name='Job_chef')
    
    
    
    
    
    
   les models de conf
   #l'image la description en pas du welcome sur la page about
   class About(models.Model):
   
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
    
    #les specialité sur la mm page
class Recipe(models.Model):

    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=True)
# Create your models here.

#pour les logo de la page 
class Change(models.Model):

    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut =  models.BooleanField(default=True) 
    
#le dishes ici affiche les menu au niveau de la navbar le dropdown special, il affiche les differents menu du singles_dishes de l'appli resto ,donc la class dishes permet de mettre le nom des different menu de single dishes et de l'afficher au niveau de la navbar
class Dishes(models.Model):

    name_plat = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)  
    statut =  models.BooleanField(default=True) 
   
    
    
    def __str__(self):
        return self.name
    
#change cest pour le logo et autre sur les differentes pages
class Change(models.Model):

    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    statut =  models.BooleanField(default=True) 
