def est_premier(n):
    for c in range(1, n):
        if c % n == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(1, 5):
        print(f"Numéro {i} premier ?? => ", est_premier(i))
