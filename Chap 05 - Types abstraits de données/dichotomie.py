from pile import *
from file import *
from timeit import default_timer as timer
import sys

def dichotomie(exp):
    """
    - Entrée : Polonais inversé
    - Sortie : Résultat du calcul
    """
    pile=pileCree()
    for k in range(len(exp)):
        if exp[k].isdigit():
            pileEmpiler(pile,exp[k])
        elif exp[k] in ["+","-","*","/"]:
            c2=pileDepiler(pile)
            c1=pileDepiler(pile)
            if exp[k]=='+':
                cal=int(c1)+int(c2)
                pileEmpiler(pile,cal)
            elif exp[k]=='-':
                cal=int(c1)-int(c2)
                pileEmpiler(pile,cal)
            elif exp[k]=='*':
                cal=int(c1)*int(c2)
                pileEmpiler(pile,cal)
            elif exp[k]=='/':
                cal=int(c1)/int(c2)
                pileEmpiler(pile,cal)
    return pile

def dicho_rec(T,x,l,r):
    """
    On cherche dans un tableau T la
    valeur x entre T[l] et T[r]
    avec l ≤ 3
    (on suppose que T est trié)
    Sortie : vrai ou faux
    """
    if l==r:
        return T[l] == x
    m = (l+r)//2
    if T[m] < x:
        return dicho_rec(T,x,m+1,r)
    if T[m] > x:
        return dicho_rec(T,x,l,m)

def dicho_ite(T,x,l,r):
    while l<=r:
        m = (l+r)//2
        if T[m] == x:
            return True
        elif T[m] < x:
            l = m+1
        else:
            r = m-1
    return False

l=0
r=60000
x=4
T=[i for i in range(1000000000)]

debut1 = timer()
print(dicho_rec(T,x,l,r))
fin1 = timer()
temps1 = fin1 - debut1
print(temps1)
debut2 = timer()
print(dicho_ite(T,x,l,r))
fin2 = timer()
temps2 = fin2 - debut2
print(temps2)
print(" ")
if temps2 > temps1:
    print("La version itérative ")
