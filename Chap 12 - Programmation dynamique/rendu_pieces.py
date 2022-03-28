EUROS = [100, 50, 20, 10, 5, 2, 1]

def glouton(somme):
    rendu = []
    somme_restante = somme
    for e in EUROS:
        while somme_restante >= e:
            somme_restante -= e
            rendu.append(e)
    return rendu

rendu = glouton(78)

print(" ")
print(rendu)
print("Nombre de pièces : " + str(len(rendu)))
print(" ")
