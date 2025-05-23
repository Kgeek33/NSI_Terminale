def fibo_rec(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)


if __name__ == '__main__':
    for n in range(11):
        print(f"Fibonacci de {n} =>", fibo_rec(n))
