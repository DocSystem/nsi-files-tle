from math import inf
import networkx as nx
import matplotlib.pyplot as plt

class Point:
    def __init__(self, nom, predecesseur = None):
        self.nom = nom
        self.couleur = "blanc"
        self.distance = inf
        self.predecesseur = predecesseur
        self.date = inf
        self.fin = inf

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

def PP(g):
    for i in g:
        i.couleur = "blanc"
        i.predecesseur = None
    global date
    date = 0
    for i in g:
        if i.couleur == "blanc":
            PP_visiter(g, i)

def PP_visiter(graphe, point):
    global date
    point.couleur = "gris"
    date += 1
    point.date = date
    for voisin in graphe[point]:
        if voisin.couleur == "blanc":
            voisin.predecesseur = point
            PP_visiter(graphe, voisin)
    date += 1
    point.couleur = "noir"
    point.fin = date

# a = Point("a")
# b = Point("b")
# c = Point("c")
# d = Point("d")
# e = Point("e")
# f = Point("f")
# g = {a: [b, d], b: [a, c, e], c: [b], d: [a], e: [b, f], f: [e]}

# v = Point("v")
# r = Point("r")
# s = Point("s")
# w = Point("w")
# t = Point("t")
# u = Point("u")
# x = Point("x")
# y = Point("y")
# g = {v: [r], r: [s, v], s: [r, w], w: [s, t, x], t: [w, u], u: [t, x, y], x: [w, u, y], y: [u, x]}

# Points de a à h
# pA = Point("a")
# pB = Point("b")
# pC = Point("c")
# pD = Point("d")
# pE = Point("e")
# pF = Point("f")
# pG = Point("g")
# pH = Point("h")
# g = {pA: [pB, pE], pB: [pC, pD], pC: [pG], pD: [pC], pE: [pF], pF: [pB], pG: [], pH: [pD]}

a = Point("a")
b = Point("b")
c = Point("c")
d = Point("d")
e = Point("e")
f = Point("f")
pG = Point("g")
g = {a: [b, d], b: [c, e], c: [], d: [], e: [], f: [a], pG: [b, d]}

# PL(g, pA)
# for p in g:
    # print(p.nom, p.distance)

PP(g)
for p in g:
    print(p.nom, p.date, p.fin)

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

# chemin = trouver_chemin(g, pA, pG)

# G = nx.Graph()
# for i in g:
#     for j in g[i]:
#         if i in chemin and j in chemin:
#             G.add_edge(i.nom, j.nom, color='red')
#             print("Ajout du chemin entre " + i.nom + " et " + j.nom)
#         else:
#             G.add_edge(i.nom, j.nom, color='black')
# colors = [G[u][v]['color'] for u,v in G.edges()]
# nx.draw(G, with_labels=True, font_weight='bold', node_size=800, node_color='lightgray', edge_color=colors)
# plt.show()
