def pileCree():
    return []

def pileTaille(P):
    return len(P)

def pileEstVide(P):
    return pileTaille(P) == 0

def pileEmpiler(P, e):
    P.append(e)

def pileDepiler(P):
    if pileEstVide(P):
        return None
    return P.pop()

def pileDepilerTete(P):
    if pileEstVide(P):
        return None
    e = P[0]
    del P[0]
    return e

def pileSommet(P):
    if pileEstVide(P):
        return None
    return P[-1]