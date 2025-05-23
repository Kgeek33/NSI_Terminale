def fibo_rec(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)

