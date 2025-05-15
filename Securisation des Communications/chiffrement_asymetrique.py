from math import sqrt


def est_premier(n):
    for p in range(2, int(sqrt(n))+1):
        if n % p == 0:
            return False
    return True


def facteurs_premiers(n: int) -> list[int]:
    UNEliste = []
    THEpremier = 2
    while n != 1:
        if n % THEpremier == 0 and est_premier(THEpremier):
            n //= THEpremier
            UNEliste.append(THEpremier)
        else:
            THEpremier += 1
    return UNEliste


def factorisation_RSA(n: int) -> list[int]:
    f = facteurs_premiers(n)
    if len(f) == 2:
        return f
    else:
        return None


def recur_pgcd(a: int, b: int) -> int:
    if b > 0:
        return recur_pgcd(b, a % b)
    return a


def premiers_entre_eux(a: int, b: int) -> bool:
    if recur_pgcd(a, b) == 1:
        return True
    return False


def cles_valides(n: int, e: int, d: int) -> bool:
    produitN = factorisation_RSA(n)
    p, q = produitN
    f = (p - 1) * (q - 1)

    test1 = premiers_entre_eux(e, f)
    test2 = p != q and p >= 3 and q >= 3
    test3 = e >= 1 and e < f
    test4 = d >= 1 and d < f
    test5 = e * d % f == 1

    return test1 and test2 and test3 and test4 and test5


if __name__ == "__main__":
    # Question 1
    for i in range(1, 10):
        print(f"Numéro {i} premier ?? => ", est_premier(i))

    # Question 2
    assert facteurs_premiers(300) == [2, 2, 3, 5, 5], "PAS BON"

    # Question 3
    print(factorisation_RSA(377))
    print(factorisation_RSA(437))
    print(factorisation_RSA(99400891))
    # print(factorisation_RSA(99999640000243))

    # Question 4
    print(premiers_entre_eux(2, 3))
    print(premiers_entre_eux(2, 5))
    print(premiers_entre_eux(2, 4))

    # Question 5
    print(
        "Clés (5, 377) et (269, 377) valides ? =>",
        cles_valides(377, 5, 269)
    )
    print(
        "Clés (2, 377) et (269, 377) valides ? =>",
        cles_valides(377, 2, 269)
    )
