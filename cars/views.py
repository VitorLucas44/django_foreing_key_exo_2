from django.shortcuts import render
from .models import Voiture, Couleur

def liste_voitures(request):
    voitures = Voiture.objects.all()
    return render(request, 'testdjango/cars/liste_voitures.html', {'voitures': voitures})

def voitures_par_couleur(request):
    couleurs = Couleur.objects.all()
    return render(request, 'testdjango/cars/voitures_par_couleur.html', {'couleurs': couleurs})
