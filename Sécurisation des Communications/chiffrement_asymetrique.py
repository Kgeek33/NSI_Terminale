def est_premier(n):
    return n % 1 == 0 and n % n == 0


print(est_premier(3))
