def est_premier(n):
    for c in range(1, n):
        if c % n == 0:
            return False
    return True
