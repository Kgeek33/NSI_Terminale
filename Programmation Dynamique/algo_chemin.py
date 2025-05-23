def chemin(n: int, m: int):
    if n == 0 or m == 0:
        return 1
    return chemin(n-1, m) + chemin(n, m-1)


if __name__ == '__main__':
    print(chemin(1, 4))
    print(chemin(3, 4))
    print(chemin(10, 10))
