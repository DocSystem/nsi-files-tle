def PLSC(X, Y):
    m = len(X)
    n = len(Y)
    X = "0" + X
    Y = "0" + Y
    TAB = [[0]*(n+1) for _ in range(m+1)]
    SOL = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i] == Y[j]:
                SOL[i][j] = SOL[i-1][j-1] + 1
                TAB[i][j] = "Diag-gauche"
            elif SOL[i-1][j] >= SOL[i][j-1]:
                SOL[i][j] = SOL[i-1][j]
                TAB[i][j] = "haut"
            else:
                SOL[i][j] = SOL[i][j-1]
                TAB[i][j] = "gauche"
    return SOL, TAB

# print(PLSC("ABCBDAB", "BDCABA")[0])
# print(PLSC("53216", "524317"))

"""
# NE MARCHE PAS

def afficher_PLSC(TAB, Y, i, j):
    if i==0 or j==0:
        return
    if TAB[i][j] == "Diag-gauche":
        afficher_PLSC(TAB, Y, i-1, j-1)
        print(Y[i-1], end="")
    elif TAB[i][j] == "haut":
        afficher_PLSC(TAB, Y, i-1, j)
    else:
        afficher_PLSC(TAB, Y, i, j-1)

X = "53216"
Y = "524317"
SOL, TAB = PLSC(X, Y)
print(TAB)
m = len(X)
n = len(Y)
afficher_PLSC(TAB, Y, m, n)
print("")
"""