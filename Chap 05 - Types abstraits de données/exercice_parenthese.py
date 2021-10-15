"""
import pile
def check_parenthese(chaine):
    p = pile.pileCree()
    for i in chaine:
        if i == "(":
            pile.pileEmpiler(p, i)
        elif i == ")":
            if pile.pileDepiler(p) == None:
                return "mal"
    return "bien" if pile.pileEstVide(p) else "mal"
"""

from pile_classe import *

def check_parenthese(chaine):
    p = Pile()
    for i in chaine:
        if i == "(":
            p.empiler(i)
        elif i == ")":
            if p.depiler() == None:
                return "mal"
    return "bien" if p.estVide() else "mal"