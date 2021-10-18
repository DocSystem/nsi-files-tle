from pile import *

def puissance_iter(x, n):
    t=0
    for _ in range(n):
        t*=x
    return t

def puissance_rec(x, n):
    if n==0:
        return 1
    return x*puissance_rec(x, n-1)

def puissance_pile(x, n):
    t=pileCree()
    for _ in range(n): pileEmpiler(t, x)
    n=1
    while len(t) > 0: n*=pileDepiler(t)
    return n

def factorielle_pile(n):
    t=pileCree()
    for i in range(1, n+1): pileEmpiler(t, i)
    n=1
    while len(t) > 0: n*=pileDepiler(t)
    return n

def puissance_rec2(x, n):
    if n==0:
        return 1
    if n%2==0:
        return puissance_rec2(x, n/2)**2
    else:
        return x*puissance_rec2(x, (n-1)/2)**2
