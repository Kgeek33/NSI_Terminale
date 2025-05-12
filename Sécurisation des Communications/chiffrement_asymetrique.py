def est_premier(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(est_premier(9967))
print(est_premier(9973))
print(est_premier(9972))

