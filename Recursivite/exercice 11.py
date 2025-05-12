def carre_diviseur(A):
    c = 0
    while A % 2 == 0:
        A /= 2
        c += 1
    return c


print(carre_diviseur(7000))
assert carre_diviseur(7000) == 10
