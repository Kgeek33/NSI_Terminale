from math import sqrt


def est_premier(n):
    for p in range(2, int(sqrt(n))+1):
        if n % p == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(1, 10):
        print(f"Numéro {i} premier ?? => ", est_premier(i))
