class rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def calcul_aire(self):
        return self.longueur * self.largeur

rect1 = rectangle(6, 4)
# print(rect1.longueur)
# print(rect1.largeur)
# print(rect1.calcul_aire())

class chien:
    def __init__(self, nom, age, race):
        self.nom = nom
        self.age = age
        self.race = race

chien1 = chien("Medor", 2, "Berger Allemand")

def affiche_information(self):
    return "Ce chien de la race " + self.race + " a pour nom " + self.nom + " et pour age " + str(self.age) + " ans(s)."

print(affiche_information(chien1))