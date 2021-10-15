def division_euclidienne_i(a, b):
    q=0
    while a>=b:
        a=a-b
        q=q+1
    return q,a

def division_euclidienne_r(a, b, q=0):
    if a<b:
        return q,a
    else:
        return division_euclidienne_r(a-b, b, q+1)
