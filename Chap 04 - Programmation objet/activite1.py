## Exercice 1

class Voiture:
    def __init__(self, couleur, kilometrage):
        self.couleur = couleur
        self.kilometrage = kilometrage

voiture1 = Voiture("bleue", 20000)
voiture2 = Voiture("rouge", 30000)

## Exercice 2

class Film:
    def __init__(self, titre, realisateur):
        self.titre = titre
        self.realisateur = realisateur

class Personne:
    def __init__(self, nom, annee_naissance, lieu_naissance):
        self.nom = nom
        self.annee_naissance = annee_naissance
        self.lieu_naissance = lieu_naissance

# Question 1

lautner = Personne("Georges Lautner", 1926, "Nice")

# Question 2

print(lautner.nom + " est une personne née à " + lautner.lieu_naissance + " en " + str(lautner.annee_naissance))

# Question 3

tonton = Film("Les tontons flingueurs", lautner)

"""
a)
Cette instruction affiche "Les tontons flingueurs"

b)
Cette instruction affiche "Georges Lautner"
"""

# c)

print(tonton.titre + " est un film réalisé par " + tonton.realisateur.nom + " originaire de " + tonton.realisateur.lieu_naissance)
