def chemin(n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 1
    return chemin(n-1, m) + chemin(n, m-1)


if __name__ == '__main__':
    assert chemin(0, 4) == 1
    assert chemin(3, 4) == 35
    assert chemin(10, 10) == 184756
