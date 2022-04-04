def parcours_largeur(G, S):
    """
    G est le graphe
    S est l'origine
    
    Pour chaque sommet u appartenant à G.S \ {S}:
        u.couleur = blanc
        u.distance = infini
        u.parent = None
    s.couleur = blanc
    s.distance = 0
    s.parent = None
    F est une file vide
    """
    