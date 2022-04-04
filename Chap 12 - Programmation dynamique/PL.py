from math import inf

class Point:
    def __init__(self, nom, predecesseur = None):
        self.nom = nom
        self.couleur = "blanc"
        self.distance = inf
        self.predecesseur = predecesseur

def enfiler(F, x):
    F.append(x)
def defiler(F):
    return F.pop(0)
def fileestvide(F):
    return len(F) == 0

# a = Point("a")
# b = Point("b")
# c = Point("c")
# d = Point("d")
# g = {a: [b, c], b: [a, d], c: [a], d: [b]}

def PL(g, s):
    for i in g:
        i.couleur = "blanc"
        i.distance = inf
        i.predecesseur = None
    s.couleur = "gris"
    s.distance = 0
    s.predecesseur = None
    F = []
    enfiler(F, s)
    while not fileestvide(F):
        u = defiler(F)
        for v in g[u]:
            if v.couleur == "blanc":
                v.couleur = "gris"
                v.distance = u.distance + 1
                v.predecesseur = u
                enfiler(F, v)
        u.couleur = "noir"

a = Point("a")
b = Point("b")
c = Point("c")
d = Point("d")
e = Point("e")
f = Point("f")
G = {a: [b, d], b: [a, c, e], c: [b], d: [a], e: [b, f], f: [e]}

PL(G, a)
for p in [a, b, c, d, e, f]:
    print(p.nom, p.distance)
