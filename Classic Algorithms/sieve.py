def sieve(l):
    d = dict.fromkeys(range(2,l+1), True)
    for i in range(2,l+1):
        if d[i]:
            for j in range(i*2, l+1, i):
                d[j] = False
    return [x for x in d if d[x]]
print sieve(30)