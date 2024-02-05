from django.db import models

class Collaborateur(models.Model):
    Statut = models.CharField(max_length=10)
    Nom = models.CharField(max_length=10)
    Prenom = models.CharField(max_length=10)
    Sexe = models.CharField(max_length=5)
    Date_de_naissance = models.DateField()
    Age = models.IntegerField()
    Situation_familiale = models.CharField(max_length=10, null=True,blank=True)
    Nombre_d_enfants = models.FloatField( null=True,blank=True)
    N_CIN =models.CharField(max_length=12 ,null=True,blank=True)
    N_Passeport=models.CharField(max_length=30 ,null=True,blank=True)
    Nationalité=models.CharField(max_length=20)
    Adresse_postale=models.CharField(max_length=50)
    Ville=models.CharField(max_length=20)
    E_mail= models.EmailField()
    N_de_téléphone=models.CharField(max_length=20)
    RIB = models.CharField(max_length=30)
    N_CNSS= models.CharField(max_length=20)
    Type_de_contrat= models.CharField(max_length=10)
    Rémunération = models.IntegerField()
    Prime = models.FloatField( null=True,blank=True)
    Poste = models.CharField(max_length=10)
    Date_d_entrée = models.DateField(null=True,blank=True)
    Date_de_Sortie = models.DateField(null=True,blank=True)
    
    def __str__(self): 
        return str(self.Nom)