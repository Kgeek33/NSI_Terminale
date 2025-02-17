def diviser(lst):
    """
    prend une liste lst
    renvoie deux listes correspondant à la moitié droite et à la moitié gauche
    """
    milieu = len(lst)//2
    return lst[:milieu], lst[milieu:]


def recherche_dichotomique(t: list[int], v: int, g: int = 0):
    if len(t) == 0:
        return None
    moitie = len(t) // 2

    if v < t[moitie]:
        return recherche_dichotomique(t[:moitie], v, g)

    if v > t[moitie]:
        return recherche_dichotomique(t[moitie + 1:], v, g + moitie + 1)

    print("dico copie trouvé!", g + moitie)
    return g + moitie


if __name__ == '__main__':
    def nextFibo(um2, um1):
        return um1, um2+um1

    def seqFibo(n):
        umoins2 = 0
        umoins1 = 1
        F = [umoins2, umoins1]
        for i in range(2, n):
            umoins2, umoins1 = nextFibo(umoins2, umoins1)
            F.append(umoins1)
        return F

    T = seqFibo(16)
    print(T)
    print("55 est à la position", recherche_dichotomique(T, 55))  # -> 10
    print("56 est à la position", recherche_dichotomique(T, 56))  # -> None
    print("377 est à la position", recherche_dichotomique(T, 377))  # -> 14
    print("610 est à la position", recherche_dichotomique(T, 610))  # -> 14
    # -> None
    print("10000 est à la position", recherche_dichotomique(T, 10000))
    print(recherche_dichotomique([0, 1, 1, 2, 3, 5, 8, 13, 21], 7))
    T = seqFibo(32)
    print(T)
    print("55 est à la position", recherche_dichotomique(T, 55))
    # -> 27
    print("196418 est à la position", recherche_dichotomique(T, 196418))
