def fact(n):
    '''
    paramètre n : (int) un entier
    valeur renvoyée : (int) la factorielle de n

    précondition : n>=0

    Exemples :
    >>> fact(3)
    6
    >>> fact(5)
    120
    >>> [fact(k) for k in range(6)]
    [1, 1, 2, 6, 24, 120]
    '''
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
