def moyenne(notes: list[tuple]) -> float:
    moy: int | float = 0
    for i in notes:
        moy += i[0] * i[1]
    for i in notes:
        moy /= i[1]
    return moy


assert moyenne([(15.0, 2), (9.0, 1), (12.0, 3)]) == 12.5


def ligne_suivante(ligne: list[int]) -> list[int]:
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1]
    for i in range(1, len(ligne)):
        ligne_suiv.append(ligne[i - 1] + ligne[i])
    ligne_suiv.append(1)
    return ligne_suiv


def pascal(n: int) -> list[list[int]]:
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [[1]]
    for k in range(n):
        ligne_k = ligne_suivante(triangle[k])
        triangle.append(ligne_k)
    return triangle


assert ligne_suivante([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
