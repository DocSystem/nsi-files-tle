def tri_iteratif(tab):
    for k in range(len(tab), 0, -1):
        imax = 0
        for i in range(0, k):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k-1] :
            tab[k-1], tab[imax] = tab[imax], tab[k-1]
    return tab

"""
def tri_iteratif_1(tab):
    M=tab[0]
    iM = 0
    for i in range(len(tab)):
        if tab[i]>M:
            M=tab[i]
            iM=i
    if M>tab[-1]:
        tab[iM] = tab[-1]
        tab[-1] = M
    return tab
"""