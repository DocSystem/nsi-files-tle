def tri_iteratif(tab):
    for k in range(len(tab), 0, -1):
        imax = 0
        for i in range(0, k):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k-1] :
            tab[k-1], tab[imax] = tab[imax], tab[k-1]
    return tab
