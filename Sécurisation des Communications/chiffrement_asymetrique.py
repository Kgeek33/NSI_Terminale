from math import sqrt


def est_premier(n):
    for p in range(2, int(sqrt(n))+1):
        if n % p == 0:
            return False
    return True


def facteurs_premiers(n: int) -> list[int]:
    UNEliste = []
    while n > 0:
        for i in range(2, 10):
            if est_premier(n % i):
                UNEliste.append(n % i)
                n /= 2
    print(UNEliste)
    return UNEliste


if __name__ == "__main__":
    for i in range(1, 10):
        print(f"Numéro {i} premier ?? => ", est_premier(i))
    assert facteurs_premiers(300) == [2, 2, 3, 5, 5], "PAS BON"
