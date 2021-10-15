### Suites basiques ###

## Fonction itérative

def u_i(a,r,n):
    """
    ENTRÉES :
    - La variable a correspond au terme du rang 0
    - La variable r correspond à la raison de la suite
    - La variable n correspond au rang du terme u(n)
    SORTIES :
    - La variable s correspond à u(n) à la fin de la fonction
    """
    s=a
    for _ in range(n):
        s*=r
    return s

## Fonction récursive

def u_r(n):
    """
    ENTRÉES :
    - La variable n correspond au rang du terme u(n)
    SORTIES :
    - Si n = 0, renvoie le premier terme (ici 2), sinon renvoie 3*u(n-1)
    """
    if n==0:
        return 2
    else:
        return 3*u_r(n-1)

### Suites de Fibonacci ###

## Fonction récursive fibonacci

def fib_r(n,a,b):
    """
    ENTRÉES :
    - La variable n correspond au rang du terme fib(n)
    - La variable a correspond au terme du rang 0 (premier terme)
    - La variable b correspond au terme du rang 1 (deuxième terme)
    SORTIES :
    - Si n = 0, renvoie a
    - Si n = 1, renvoie b
    - Sinon, renvoie fib(n-1)+fib(n-2)
    """
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fib_r(n-1,a,b)+fib_r(n-2,a,b)

## Fonction itérative fibonacci

def fib_i(n,a,b):
    """
    ENTRÉES :
    - La variable n correspond au rang du terme fib(n)
    - La variable a correspond au terme du rang 0 (premier terme)
    - La variable b correspond au terme du rang 1 (deuxième terme)
    SORTIES :
    - Le terme de rang n
    """
    if n==0:
        return a
    elif n==1:
        return b
    else:
        u=a
        v=b
        for i in range(2, n+1):
            w=u+v
            u=v
            v=w
        return w


n=40

"""
On teste la fonction pour la suite géométrique suivante :
u(0) = 1
r = 3
On cherche u(3)
"""
# print(u_i(2,3,n))
# print(u_r(n))

# print(fib_r(n,1,1))
# print(fib_i(n,1,1))

### Factorielle ###

## Factorielle itérative

def fact_i(n):
    if n==0: return 1
    f=1
    for i in range(1,n+1): f*=i
    return f

## Factorielle récursive

def fact_r(n):
    if n==0: return 1
    return n*fact_r(n-1)

# print(fact_r(5))
# print(fact_i(5))

### Palindrome ###

## Palindrome itératif // FAUX

# def pal_i(w):
    # if len(w)==0 or len(w)==1: return True
    # if w[0] == w[-1] and w[1] == w[-2]: return True
    # else: return False

## Palindrome récursif

def pal_r(w):
    if len(w)==0 or len(w)==1: return True
    if w[0]==w[-1]: return pal_r(w[1:-1])
    else: return False

# print(pal_r("radar"))
# print(pal_r("antilope"))
