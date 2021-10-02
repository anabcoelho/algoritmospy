def divide_and_conquer(p, q):
    n = len(p)  # assume que p e q tem o mesmo grau
    if n == 1:
        r = [0]
        r[0] = p[0] * q[0]
        return (r)
    z = int(n / 2)
    p_e = p[0:z]
    p_d = p[z:n]
    q_e = q[0:z]
    q_d = q[z:n]
    r = []
    for i in range(2 * n - 1):
        r.append(0)

    res1 = divide_and_conquer(p_e, q_e)
    res2 = divide_and_conquer(p_e, q_d)
    res3 = divide_and_conquer(p_d, q_e)
    res4 = divide_and_conquer(p_d, q_d)
    # formula mágica:pe(x)⋅qe(x)+
    # (pe(x)⋅qd(x)+pd(x)⋅qe(x))x^n/2+
    # (qd.qe)x^n
    for i in range(len(res1)):  # pe(x)⋅qe(x)
        r[i] = r[i] + res1[i]
    for i in range(len(res2)):  # (pe(x)⋅qd(x)+
        r[z + i] = r[z + i] + res2[i]
    for i in range(len(res3)):  # pd(x)⋅qe(x)(z+i para ocupar os espaços do x^2)
        r[z + i] = r[z + i] + res3[i]
    for i in range(len(res4)):  # qd.qe (após o máximo do polinômio até o grau 2n-2)
        r[n + i] = r[n + i] + res4[i]
    return (r)


a = [6, 8, 2, 1]
b = [3, 5, 6, 7]
print(divide_and_conquer(a, b))