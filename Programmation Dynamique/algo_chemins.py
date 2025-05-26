def chemin(n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 1
    return chemin(n - 1, m) + chemin(n, m - 1)


def chemins_memo(n: int, m: int, dico: dict[tuple, int] = {}) -> int:
    if n == 0 or m == 0:
        return 1
    if (n, m) in dico:
        return dico[(n, m)]

    dico[(n, m)] = chemins_memo(n-1, m) + chemins_memo(n, m-1)

    return dico[(n, m)]


def chemins_dyn(n: int, m: int) -> int:
    tab = [[1] * (m+1)] * (n+1)
    for k in range(1, n+1):
        for g in range(1, m+1):
            tab[k][g] = tab[k-1][g] + tab[k][g-1]
    return tab[n][m]


if __name__ == '__main__':
    assert chemin(0, 4) == 1
    assert chemin(10, 10) == 184756
    assert chemin(3, 4) == 35
    assert chemins_memo(0, 4) == 1
    assert chemins_memo(3, 4) == 35
    assert chemins_memo(10, 10) == 184756
    assert chemins_dyn(0, 4) == 1
    assert chemins_dyn(3, 4) == 35
    assert chemins_dyn(10, 10) == 184756
