def fibo_rec(n):
    if n == 0 or n == 1:
        return 1
    return fibo_rec(n-1) + fibo_rec(n-2)


if __name__ == '__main__':
    assert fibo_rec(4) == 5
    assert fibo_rec(5) == 8
    assert fibo_rec(6) == 13
    assert fibo_rec(7) == 21
    assert fibo_rec(8) == 34
    assert fibo_rec(9) == 55
    assert fibo_rec(10) == 89
