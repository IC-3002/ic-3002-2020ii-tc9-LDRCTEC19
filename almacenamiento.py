def maximizar(As, D):
    M = []
    c = 0
    for x in As:
        aux = As[x][1]
        if (c + aux) < D:
            c += aux
            M.append(As[x])
    return M