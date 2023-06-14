from cars.models import Voiture, Couleur

def run():
    # Création des couleurs
    couleur_rouge = Couleur.objects.create(nom="Rouge")
    couleur_bleu = Couleur.objects.create(nom="Bleu")
    couleur_vert = Couleur.objects.create(nom="Vert")
    couleur_noir = Couleur.objects.create(nom="Noir")

    # Création des voitures
    Voiture.objects.create(marque="Renault", annee_creation=2020, couleur=couleur_rouge)
    Voiture.objects.create(marque="BMW", annee_creation=2018, couleur=couleur_bleu)
    Voiture.objects.create(marque="Golf", annee_creation=2022, couleur=couleur_vert)
    Voiture.objects.create(marque="Tesla", annee_creation=2019, couleur=couleur_noir)
