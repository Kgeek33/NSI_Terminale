def renverse(pile: list[int]):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        a = pile.pop()
        if a >= 0:
            pile_positifs.append(a)
    return renverse(pile_positifs)


assert renverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positifs([-2]) == []
