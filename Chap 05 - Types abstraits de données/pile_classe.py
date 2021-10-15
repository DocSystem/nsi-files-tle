class Cellule:
    def __init__(self, valeur=None, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class Pile:
    def __init__(self):
        self.top = None
    def estVide(self):
        return self.top == None
    def empiler(self, element):
        nouvelleCellule = Cellule(element, self.top)
        self.top = nouvelleCellule
    def depiler(self):
        if not self.estVide():
            valeur = self.top.valeur
            self.top = self.top.suivant
            return valeur
        else:
            return None
