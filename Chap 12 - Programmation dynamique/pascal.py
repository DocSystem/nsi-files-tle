# Question 2
def binomial_rec(n, m):
    if m == 0 or m == n:
        return 1
    else:
        return binomial_rec(n - 1, m) + binomial_rec(n - 1, m - 1)

print(binomial_rec(4, 2))

# Question 4
def binomial_dyn(n, m):
    K = [[-1] * (n + 1) for i in range(n + 1)]
    K[0][0] = 1
    K[1][0], K[1][1] = 1, 1
    for i in range(2, n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                K[i][j] = 1
            else:
                K[i][j] = K[i - 1][j - 1] + K[i - 1][j]
    return K[n][m]

print(binomial_dyn(4, 2))

# Question 5
def binomial_memoise(n, m, K):
    if m == 0 or m == n:
        return 1
    else:
        if K[n][m] == -1:
            K[n][m] = binomial_memoise(n - 1, m, K) + binomial_memoise(n - 1, m - 1, K)
        return K[n][m]

def binomial(n, m):
    K = [[-1] * (n + 1) for i in range(n + 1)]
    K[0][0] = 1
    K[1][0], K[1][1] = 1, 1
    return binomial_memoise(n, m, K)

print(binomial(4, 2))
