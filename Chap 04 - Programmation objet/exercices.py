from math import sqrt
import matplotlib.pyplot as plt

## EXERCICE 1

class Point:
    def __init__(self, nom, x, y):
        self.nom = nom
        self.abscisse = x
        self.ordonnee = y
    
    def affichage(self):
        print("Nom : " + self.nom)
        print("Abscisse : " + str(self.abscisse))
        print("Ordonnée : " + str(self.ordonnee))

pt1 = Point("A", 3, 5)
pt2 = Point("B", 11, 1)
pt3 = Point("C", 2, -1)

def calc_distance(a, b):
    x1 = a.abscisse
    x2 = b.abscisse
    y1 = a.ordonnee
    y2 = b.ordonnee
    return sqrt((x2-x1)**2 + (y2-y1)**2)

## EXERCICE 2

class Triangle:
    def __init__(self, sommet1, sommet2, sommet3):
        self.sommet1 = sommet1
        self.sommet2 = sommet2
        self.sommet3 = sommet3
        self.cote1 = calc_distance(sommet1, sommet2)
        self.cote2 = calc_distance(sommet2, sommet3)
        self.cote3 = calc_distance(sommet3, sommet1)
    def perimetre(self):
        return self.cote1 + self.cote2 + self.cote3
    def PG_cote(self):
        l = self.cote1
        if (self.cote2 > l):
            l = self.cote2
        if (self.cote3 > l):
            l = self.cote3
        return l
    def __eq__(self, other):
        return self.cote1 == other.cote1 and self.cote2 == other.cote2 and self.cote3 == other.cote3
    def estAplati(self):
        return (self.cote1 == self.cote2 + self.cote3) or (self.cote2 == self.cote1 + self.cote3) or (self.cote3 == self.cote1 + self.cote2)
    def afficher(self):
        X = [self.sommet1.abscisse, self.sommet2.abscisse, self.sommet3.abscisse, self.sommet1.abscisse]
        Y = [self.sommet1.ordonnee, self.sommet2.ordonnee, self.sommet3.ordonnee, self.sommet1.ordonnee]
        plt.axis("equal")
        plt.plot(X,Y)
        plt.show()

tri1 = Triangle(Point("A", 1, 1), Point("B", 3, 1), Point("C", 1, 3))

