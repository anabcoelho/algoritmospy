def som_pol(x, y):
    a = len(x)
    b = len(y)
    r = []
    # bloco da lista do 0
    if a >= b:
        m = a - b
        min = b
        for i in range(a):
            r.append(0)
    else:  # a < b
        m = b - a
        min = a
        for i in range(b):
            r.append(0)
    print(r)

    # bloco da soma
    x.reverse()
    y.reverse()
    t = 0
    print(x)
    print(y)
    print(min)
    for i in range(min):
        r[i] = x[i] + y[i]
        print(r[i], x[i], y[i])
        print("i", i)
        t = t + 1
    print(r)
    r.reverse()
    x.reverse()
    y.reverse()
    print(r)
    if t != len(r):
        for j in range(m):
            if a > b:
                r[j] = x[j]
                print(x[j])
            else:
                r[j] = y[j]
                print(y[j])

    return (r)


u = [7, 6, 4, 5, 9]
j = [1, 2, 3]
print(som_pol(u, j))