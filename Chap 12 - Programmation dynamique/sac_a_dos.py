# poidsMax = 8
# poids = [3, 4, 5, 4, 2]
# valeurs = [15, 18, 20, 12, 6]
# poidsMax = 12
# poids = [1, 2, 5, 6, 7]
# valeurs = [1, 6, 18, 22, 24]
# poidsMax = 12
# poids = [1, 2, 5, 6, 7]
# valeurs = [1, 6, 18, 22, 24]
poidsMax = 10
poids = [5, 4, 6, 3]
valeurs = [10, 40, 30, 50]
n = len(poids)

k = valeurs[0]
objets = []

for i in range(n):
    for j in range(i+1, n):
        if poids[i] + poids[j] <= poidsMax:
            if valeurs[i] + valeurs[j] > k:
                k = valeurs[i] + valeurs[j]
                objets = [i + 1, j + 1]

print(k)
print(objets)
