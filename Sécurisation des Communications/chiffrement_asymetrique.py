from math import sqrt


def est_premier(n):
    for p in range(2, int(sqrt(n))+1):
        if n % p == 0:
            return False
    return True


def facteurs_premiers(n):
    i = 2
    r = n
    p = []
    while r != 1:
        if est_premier(i) and n % i == 0:
            p.append(i)
            r = n // i
        i += 1
    return p


print(facteurs_premiers(300))

if __name__ == "__main__":
    for i in range(1, 10):
        print(f"Numéro {i} premier ?? => ", est_premier(i))
