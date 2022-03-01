def generatesub(a):
    b = []
    n = len(a)
    e = pow(2,n)
    i = 1
    while i < e:
        j = 0
        sub = ""
        while j < n:
            if i & (1 << j):
                sub = sub + a[j]
            j = j+1
        b.append(sub)
        i = i+1
    return b