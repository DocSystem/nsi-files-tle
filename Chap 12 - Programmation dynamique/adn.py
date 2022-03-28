from json import dumps
def PLSC(X, Y):
    m = len(X)
    n = len(Y)
    X = "0" + X
    Y = "0" + Y
    TAB = [[0]*n for _ in range(m)]
    SOL = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i] == Y[j]:
                SOL[i][j] = SOL[i-1][j-1] + 1
                TAB[i-1][j-1] = "Diag-gauche"
            elif SOL[i-1][j] >= SOL[i][j-1]:
                SOL[i][j] = SOL[i-1][j]
                TAB[i-1][j-1] = "haut"
            else:
                SOL[i][j] = SOL[i][j-1]
                TAB[i-1][j-1] = "gauche"
    return SOL, TAB

print(dumps(PLSC("ABCBDAB", "BDCABA"), indent=4))
