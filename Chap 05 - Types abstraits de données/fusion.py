def fusion(t1,t2):
    t = [0 for _ in range(len(t1)+len(t2))]
    i1 = 0
    i2 = 0
    j = 0
    while i1 < len(t1) and i2 < len(t2):
        if t1[i1] <= t2[i2]:
            t[j] = t1[i1]
            i1 += 1
        else:
            t[j] = t2[i2]
            i2 += 1
        j += 1
    while i1 < len(t1):
        t[j] = t1[i1]
        i1 += 1
        j += 1
    while i2 < len(t2):
        t[j] = t2[i2]
        i2 += 1
        j += 1
    return t
