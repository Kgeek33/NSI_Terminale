def est_premier(n):
    d = []
    for i in range(2, n):
        if n % i == 0:
            d.append(i)
    return d == []


print(est_premier(9967))
print(est_premier(9973))
print(est_premier(9972))
