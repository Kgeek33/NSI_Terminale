def fibo_rec(n: int) -> int:
    if n <= 1:
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)


def fibo_memo(n, dico={}):

    if n <= 1:
        return 1
    if n in dico:
        return dico[n]
    for i in range(n):
        dico[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return dico[n]





if __name__ == '__main__':
    for n in range(11):
        print(f"Fibonacci de {n} =>", fibo_rec(n))
    for n in range(11):
        print(f"Fibonacci mémo de {n} =>", fibo_memo(n))
