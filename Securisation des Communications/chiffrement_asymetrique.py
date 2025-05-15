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


def cles_valides(n, e, d):
    cle_publique = [e, n]
    cle_privee = [d, n]
    if cle_publique[0] != cle_privee[0] and cle_publique[1] == cle_privee[1]:
        return True
    return False


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
    print(factorisation_RSA(99999640000243))

    # Question 4
    print(premiers_entre_eux(2, 3))
    print(premiers_entre_eux(2, 5))
    print(premiers_entre_eux(2, 4))
