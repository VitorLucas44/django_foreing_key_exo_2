from django.db import models

class Couleur(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    marque = models.CharField(max_length=50)
    annee_creation = models.IntegerField()
    couleur = models.ForeignKey(Couleur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marque} ({self.annee_creation})"
