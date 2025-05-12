def puissance(x, n):
    if n == 0:
        return 1

    return puissance(x, n-1) * x


assert puissance(3.0009999, 0) == 1
assert puissance(6.02, 2) == 36.240399999999994


def somme(n):
    if n <= 1:
        return 1
    return somme(n-1) + n


assert somme(-1) == 1
assert somme(5) == 15


def sommeGeo(n, u0, q):
    if n == 1:
        return u0

    return (u0 * q ** (n-1) + sommeGeo(n-1, u0, q))


nb_termes = 5
u0 = 1
q = -7
assert sommeGeo(8, 1, 2) == 255
assert sommeGeo(8, 10, 0.1) == 11.111110999999998
assert sommeGeo(nb_termes, u0, q) == 2101
