from fusion import fusion

def tri_fusion(t):
    if len(t) < 2:
        return t[:]
    t1 = t[:int(len(t)/2)]
    t2 = t[int(len(t)/2):]
    return fusion(t1,t2)
