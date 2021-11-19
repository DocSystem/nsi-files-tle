def tri(tab):
    return sorted(tab)

def moitie_gauche(tab):
    if len(tab)%2 == 0:
        s = int(len(tab)/2)
    else:
        s = int(len(tab)/2+1)
    T = []
    for i in range(s):
        T.append(tab[i])
    return T

def moitie_droite(tab):
    if len(tab)%2 == 0:
        s = int(len(tab)/2)
    else:
        s = int(len(tab)/2+1)
    T = []
    for i in range(s,len(tab)):
        T.append(tab[i])
    return T

def nb_inv_tab(tab1, tab2):
    n = 0
    for i in range(len(tab1)):
        for j in range(len(tab2)):
            if tab1[i] > tab2[j]:
                n+=1
    return n

def nb_inversions_rec(tab):
    if len(tab) <= 1:
        return 0
    tab1 = moitie_gauche(tab)
    tab2 = moitie_droite(tab)
    t = nb_inversions_rec(tab1) + nb_inversions_rec(tab2)
    tab1 = tri(tab1)
    tab2 = tri(tab2)
    t += nb_inv_tab(tab1, tab2)
    return t
