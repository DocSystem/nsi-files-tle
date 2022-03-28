def maxList(tab):
    maxi = tab[0]
    for i in range(1,len(tab)):
        if tab[i]>maxi:
            maxi = tab[i]
    return maxi

def ResoudreDyn(tab):
    G = []
    n = len(tab)
    for j in range(n):
        G.append([0]*(j+1))
    for j in range(n):
        G[n-1][j] = tab[n-1][j]
    for l in range(n-2,-1,-1):
        for r in range(l+1):
            G[l][r]=tab[l][r]+max(G[l+1][r],G[l+1][r+1])
    return G[0][0]

def Solution3(tab):
    """
    Cette fonction renvoie les valeurs du chemin parcouru dans tab par ResoudreDyn
    """
    G = []
    n = len(tab)
    for j in range(n):
        G.append([0]*(j+1))
    for j in range(n):
        G[n-1][j] = tab[n-1][j]
    for l in range(n-2,-1,-1):
        for r in range(l+1):
            G[l][r]=tab[l][r]+max(G[l+1][r],G[l+1][r+1])
    return G

tab=[[5],[8,10],[11,3,4],[6,10,7,12]]
# print(ResoudreDyn(tab))
print(Solution3(tab))