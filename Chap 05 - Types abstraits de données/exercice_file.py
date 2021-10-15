from file import *
from pile import *

"""
Exercice 2
"""
# F=fileCree()
# fileAjouterFin(F, "A")
# fileAjouterFin(F, "B")
# fileAjouterFin(F, "C")

def fileInverse(F):
    nF=fileCree()
    while len(F) > 0:
        fileAjouterFin(nF, F.pop())
    return nF

"""
Exercice 3
"""
# F=fileCree()
# fileAjouterFin(F, "L")
# fileAjouterFin(F, "L")
# fileAjouterFin(F, "C")
# fileAjouterFin(F, "L")
# fileAjouterFin(F, "C")
# fileAjouterFin(F, "C")
def rangerLapinsCarottes(F):
    lapins=fileCree()
    carottes=fileCree()
    while len(F) > 0:
        if fileTete(F)=="L":
            fileAjouterFin(lapins, fileRetirerTete(F))
        elif fileTete(F)=="C":
            fileAjouterFin(carottes, fileRetirerTete(F))
    while len(carottes) > 0:
        fileAjouterFin(F, fileRetirerTete(carottes))
    while len(lapins) > 0:
        fileAjouterFin(F, fileRetirerTete(lapins))
    return F

# P=pileCree()
# pileEmpiler(P, "L")
# pileEmpiler(P, "L")
# pileEmpiler(P, "C")
# pileEmpiler(P, "L")
# pileEmpiler(P, "C")
# pileEmpiler(P, "C")
def rangerLapinsCarottesPile(P):
    lapins=pileCree()
    carottes=pileCree()
    while not pileEstVide(P):
        if pileSommet(P) == "L":
            pileEmpiler(lapins, pileDepiler(P))
        elif pileSommet(P) == "C":
            pileEmpiler(carottes, pileDepiler(P))
    while not pileEstVide(carottes):
        pileEmpiler(P, pileDepiler(carottes))
    while not pileEstVide(lapins):
        pileEmpiler(P, pileDepiler(lapins))
    return P

"""
Exercice 5
"""

def zFileCree():
    return (pileCree(), pileCree())

def zFileTaille(F):
    if len(F[0]) > 0:
        return len(F[0])
    elif len(F[1]) > 0:
        return len(F[1])
    else:
        return 0

def zFileEstVide(F):
    return zFileTaille(F) == 0

def zFileAjouterFin(F, e):
    if len(F[0]) > 0:
        pileEmpiler(F[1], e)
        while len(F[0]) > 0:
            pileEmpiler(F[1], pileDepilerTete(F[0]))
    elif len(F[1]) > 0:
        pileEmpiler(F[0], e)
        while len(F[1]) > 0:
            pileEmpiler(F[0], pileDepilerTete(F[1]))
    else:
        pileEmpiler(F[0], e)

def zFileRetirerTete(F):
    if len(F[0]) > 0:
        return pileDepiler(F[0])
    elif len(F[1]) > 0:
        return pileDepiler(F[1])
    else:
        return None
