def rechercheMinMax(tab):
    if len(tab) > 0:
        m=tab[0]
        M=tab[0]
        for i in tab:
            if i > M:
                M=i
            if i < m:
                m=i
        return {"min": m, "max": M}
    else:
        return {"min": None, "max": None}

print(rechercheMinMax([0,1,4,2,-2,9,3,1,7,1]))
print(rechercheMinMax([]))
