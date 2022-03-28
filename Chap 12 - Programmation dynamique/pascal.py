def binomial_rec(a, b):
    if b == 0 or b == a:
        return 1
    else:
        return binomial_rec(a - 1, b) + binomial_rec(a - 1, b - 1)

# print(binomial_rec(4, 2))

def binomial_dyn(a, b):
    if b == 0 or b == a:
        return 1
    else:
        if b < a:
            return binomial_dyn(a - 1, b) + binomial_dyn(a - 1, b - 1)
        else:
            return binomial_dyn(a - 1, b)

# print(binomial_dyn(4, 2))

def binomial_memoise(a, b, K):
    if b == 0 or b == a:
        return 1
    else:
        if K[a][b] == -1:
            K[a][b] = binomial_memoise(a - 1, b, K) + binomial_memoise(a - 1, b - 1, K)
        return K[a][b]

def binomial(a, b):
    K = [[-1] * (a + 1) for i in range(a + 1)]
    K[0][0] = 1
    K[1][0], K[1][1] = 1, 1
    return binomial_memoise(a, b, K)

print(binomial(4, 2))
