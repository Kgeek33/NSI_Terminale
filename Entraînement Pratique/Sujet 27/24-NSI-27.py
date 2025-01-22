def couples_consecutifs(tab: list):
    uneliste: list[tuple] = []
    for i in range(1, len(tab)):
        if (tab[i-1] + 1 == tab[i]):
            uneliste.append((tab[i-1], tab[i]))

    return uneliste


assert couples_consecutifs([1, 4, 3, 5]) == []
assert couples_consecutifs([1, 4, 5, 3]) == [(4, 5)]
assert couples_consecutifs([1, 1, 2, 4]) == [(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4]) == [(1, 2), (3, 4)]
assert couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]
                           ) == [(1, 2), (2, 3), (-5, -4)]


def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0:
        colore_comp1(M, i-1, j, val)
    if i < len(M)-1:
        colore_comp1(M, i+1, j, val)
    if j >= 0:
        colore_comp1(M, i, j-1, val)
    if j < len(M[i])-1:
        colore_comp1(M, i, j+1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
