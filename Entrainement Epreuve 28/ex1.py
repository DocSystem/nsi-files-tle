a = {'F':['B','G'], 'B':['A','D'],'A':['',''],'D':['C','E'],'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

def taille(arbre, lettre):
    t=1
    if arbre[lettre][0] != "":
        t+=taille(arbre, arbre[lettre][0])
    if arbre[lettre][1] != "":
        t+=taille(arbre, arbre[lettre][1])
    return t

print(taille(a, "F"))