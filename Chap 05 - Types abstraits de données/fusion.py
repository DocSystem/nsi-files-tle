def fusion(t1,t2):
    t = [0 for _ in range(len(t1)+len(t2))]
    i1 = i2 = j = 0
    infini = 10**10
    t1.append(infini)
    t2.append(infini)
    while t1[i1] < infini or t2[i2] < infini:
        if t1[i1] <= t2[i2]:
            t[j] = t1[i1]
            i1 += 1
        else:
            t[j] = t2[i2]
            i2 += 1
        j += 1
    # while i1 < len(t1):
    #     t[j] = t1[i1]
    #     i1 += 1
    #     j += 1
    # while i2 < len(t2):
    #     t[j] = t2[i2]
    #     i2 += 1
    #     j += 1
    return t

print(fusion([1,3,6], [2,4,5,7,8,10]))
