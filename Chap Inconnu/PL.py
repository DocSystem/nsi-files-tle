from math import inf
import networkx as nx
import matplotlib.pyplot as plt

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

# a = Point("a")
# b = Point("b")
# c = Point("c")
# d = Point("d")
# e = Point("e")
# f = Point("f")
# g = {a: [b, d], b: [a, c, e], c: [b], d: [a], e: [b, f], f: [e]}

v = Point("v")
r = Point("r")
s = Point("s")
w = Point("w")
t = Point("t")
u = Point("u")
x = Point("x")
y = Point("y")
g = {v: [r], r: [s, v], s: [r, w], w: [s, t, x], t: [w, u], u: [t, x, y], x: [w, u, y], y: [u, x]}

PL(g, s)
for p in g:
    print(p.nom, p.distance)

# draw graph using nx
# G = nx.Graph()
# G.add_edges_from([(a.nom, b.nom), (a.nom, d.nom), (b.nom, c.nom), (b.nom, e.nom), (c.nom, b.nom), (d.nom, a.nom), (e.nom, b.nom), (e.nom, f.nom), (f.nom, e.nom)])
# nx.draw(G, with_labels=True, font_weight='bold', node_size=800, node_color='lightgray')

def trouver_chemin(graphe, point_a, point_b):
    PL(graphe, point_a)
    chemin = []
    p = point_b
    while p != None:
        chemin.append(p)
        p = p.predecesseur
    chemin.reverse()
    return chemin

chemin = trouver_chemin(g, v, y)

G = nx.Graph()
for i in g:
    for j in g[i]:
        if i in chemin and j in chemin:
            G.add_edge(i.nom, j.nom, color='red')
            print("Ajout du chemin entre " + i.nom + " et " + j.nom)
        else:
            G.add_edge(i.nom, j.nom, color='black')
colors = [G[u][v]['color'] for u,v in G.edges()]
nx.draw(G, with_labels=True, font_weight='bold', node_size=800, node_color='lightgray', edge_color=colors)
plt.show()
