import timeit


def puissance_logn(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        r = puissance_logn(x, n//2)
        if n % 2 == 0:
            return r*r
        else:
            return x*r*r


assert puissance_logn(3, 4) == 81
assert puissance_logn(3, 9) == 19683


def puissance(x, n):
    if n == 0:
        return 1

    return puissance(x, n-1) * x


print("puissance_logn :", timeit.timeit(
    lambda: puissance_logn(3, 90), number=1))
print("puissance :", timeit.timeit(lambda: puissance(3, 90), number=1))
