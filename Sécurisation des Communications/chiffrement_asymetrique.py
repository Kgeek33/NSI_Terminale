def est_premier(n):
    return n % 1 == 0 and n % n == 0


if __name__ == "__main__":
    for i in range(1, 5):
        print(f"Numéro {i} premier ?? => ", est_premier(i))
