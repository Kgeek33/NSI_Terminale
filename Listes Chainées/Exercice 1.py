def concatener(t1: list, t2: list) -> list:
    t3 = []
    for LAliste in t1, t2:
        for elm in LAliste:
            t3.append(elm)
    return t3

assert concatener([10, 20, 30], [100, 200, 300]) == [
    10, 20, 30, 100, 200, 300]

def inserer(t: list, i: int, v: int) -> list:
    # t.insert(i, v)
    t.append(None)
    for j in range(len(t) - 1, i, -1):
        t[j] = t[j-1]
    t[i] = v
    return t

assert inserer([10, 20, 30], 0, 3000) == [3000, 10, 20, 30]
