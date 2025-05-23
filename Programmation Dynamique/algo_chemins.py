def chemins_rec(n: int, m: int) -> int:
    if m == 0 or n == 0:
        return 1
    return chemins_rec(n - 1, m) + chemins_rec(n, m - 1)


if __name__ == '__main__':
    assert chemins_rec(10, 10) == 184756
