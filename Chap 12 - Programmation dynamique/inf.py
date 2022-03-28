from math import inf

def dynRecursif(valeursFaciales, somme):
    if somme < 0:
        return inf
    elif somme == 0:
        return 0
    mini = inf
    for x in valeursFaciales:
        mini = min(mini, 1 + dynRecursif(valeursFaciales, somme - x))
    return mini

def dynMemoise(v, somme):
    f = [0] * (somme + 1)
    for s in range(somme + 1):
        f[s] = inf
        for x in v:
            if s >= x:
                f[s] = min(f[s], 1 + f[s - x])
    return f, f[somme]

# print(dynMemoise([100, 50, 20, 10, 5, 2, 1], 12))
