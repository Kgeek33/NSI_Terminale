def fibo_rec(n: int) -> int:
    if n <= 1:
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_memo(n: int, dico={}):
    if n <= 1:
        return 1
    if n in dico:
        return dico[n]
    for _ in range(n):
        dico[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return dico[n]


def fibo_dyn(n):

    tab = [0]*(n+1)

    for k in range(1, n+1):

        pass


if __name__ == '__main__':
    for n in range(34):
        print(f"Fibonacci de {n} =>", fibo_rec(n))
    for n in range(34):
        print(f"Fibonacci mémo de {n} =>", fibo_memo(n))
