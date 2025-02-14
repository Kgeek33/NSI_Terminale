def fusion_iter(L, R):
    """
    prend deux listes L et R triées
    renvoie la fusion T triée des deux listes
    """
    i, j = 0, 0
    T = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            T.append(L[i])
            i += 1
        else:
            T.append(R[j])
            j += 1
    # une des deux listes est entièrement traitée
    if i >= len(L):
        # L est entièrement traitée, s'il restait des elts de R non traités
        # ils sont ajoutés à T
        T = T+R[j:]
    if j >= len(R):
        # R est entièrement traitée, s'il restait des elts de L non traités
        # ils sont ajoutés à T
        T = T+L[i:]
    # print(T)
    return T


def fusion_rec(L, R):
    """
    prend deux listes L et R triées
    renvoie la fusion T triée des deux listes
    """
    print(L, R)
    T = "a completer..."
    print(T)
    return T


def diviser(lst):
    """
    prend une liste lst et renvoie deux listes
    correspondant à la moitié droite et à la moitié gauche
    """
    return "à compléter"


def tri_fusion(lst):
    return "à compléter"


if __name__ == '__main__':

    print("test de la fusion")
    liste1 = [3, 5, 8, 9]
    liste2 = [1, 2, 6, 10, 14, 45]
    print("fusion iter {} et {} : {}".format(
        liste1, liste2, fusion_iter(liste1, liste2)))
    print("fusion iter {} et {} : {}".format(
        liste2, liste1, fusion_iter(liste2, liste1)))
#     assert fusion_iter(liste1,liste2)==fusion_rec(liste1,liste2)
#     assert fusion_iter(liste2,liste1)==fusion_rec(liste2,liste1)

    vrac = [3, 4, 6, 2, 5, 1, 8, 7]
    print("en vrac :", vrac)
    print("en ordre :", tri_fusion(vrac))

    vrac = [30, 4, 26, 28, 15, 12, 80, 71, 54]
    print("en vrac :", vrac)
    print("en ordre :", tri_fusion(vrac))
