def somme(n):
    '''
    n - entier naturel supérieur ou égal à 1
    sortie : -S  : S est la somme 1+2+...+n

    '''
    #Vérification de précondition
    assert n>=1

    #le code ci-dessous
    if n==1:
        return 1
    else:
        return n+somme(n-1)

assert somme(3)==6
