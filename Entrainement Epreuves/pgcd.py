def pgcd_i(a, b):
    """
    Tant que le reste de la divsion de a par b est non nul faire :
    * r est le reste de la division de a par b
    * b prend la valeur de r
    * a prend la valeur de b
    """
    r = b%a
    d = b
    m = a
    while r>0:
        add = d%m
        d = m
        m = add
        r = d%m
    return m

def pgcd_r(a, b):
    r = b%a
    if r==0:
        return a
    return pgcd_r(b%a, a)
