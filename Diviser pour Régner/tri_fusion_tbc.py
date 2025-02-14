def fusion_iter(L, R):
    """
    prend deux listes L et R triées
    renvoie la fusion T triée des deux listes
    """
    T = []
    i_L = 0
    i_R = 0
    while i_L < len(L) and i_R < len(R):
        if L[i_L] < R[i_R]:
            T.append(L[i_L])
            i_L += 1
        else:
            T.append(R[i_R])
            i_R += 1
    if i_L >= len(L):
        T += R[i_R:]
    if i_R >= len(R):
        T += L[i_L:]
    print(T)
    return T


def fusion_rec(L, R):
    """
    prend deux listes L et R triées
    renvoie la fusion T triée des deux listes
    """
    print(L, R)
    if R == []:
        return L
    if L == []:
        return R
    if L[0] <= R[0]:
        return [L[0]] + fusion_rec(L[1:], R)
    return [R[0]] + fusion_rec(L, R[1:])


def diviser(lst):
    """
    prend une liste lst
    renvoie deux listes correspondant à la moitié droite et à la moitié gauche
    """
    return lst[len(lst) // 2:], lst[:len(lst) // 2]


def tri_fusion(lst):
    if len(lst) < 2:
        return lst
    left, right = diviser(lst)
    # print(left, right)
    return fusion_rec(tri_fusion(left), tri_fusion(right))


if __name__ == '__main__':
    print("test de la fusion")
    liste1 = [3, 5, 8, 9]
    liste2 = [1, 2, 6, 10, 14, 45]
    print("fusion iter {} et {} : {}".format(
        liste1,
        liste2,
        fusion_iter(liste1, liste2)
    ))
    print("fusion iter {} et {} : {}".format(
        liste2,
        liste1,
        fusion_iter(liste2, liste1)
    ))
    assert fusion_iter(liste1, liste2) == fusion_rec(liste1, liste2)
    assert fusion_iter(liste2, liste1) == fusion_rec(liste2, liste1)

    print("test du tri fusion")

    vrac = [3, 4, 6, 2, 5, 1, 8, 7]
    print("en vrac :", vrac)
    print("en ordre :", tri_fusion(vrac))

    vrac = [30, 4, 26, 28, 15, 12, 80, 71, 54]
    print("en vrac :", vrac)
    print("en ordre :", tri_fusion(vrac))

    # benchs
    from tri_insertion import tri_insertion

    # from triSelectionMinimum import triSelection

    from random import randint
    # import timeit
    # import functools
    from time import perf_counter

    def unTableau(min, max, n):
        """renvoie un tableau de n entiers entre min et max compris"""
        t = []
        for i in range(n):
            t.append(randint(min, max))
        return t

    A = 0
    N = 10000
    B = A+N*10

    V = unTableau(A, B, 18)
    print("en vrac :", V)
    print("en ordre :", tri_fusion(V))

    # tests de performance
    def temps_d_exécution(f, x):
        # print("{} avec timeit et x={}".format(f,x))
        # print(timeit.timeit(functools.partial(f, x),number=1))
        print("perf_counter de {} avec n={}".format(f, len(x)))
        t1 = perf_counter()
        # r = f(x)
        t2 = perf_counter()
        print("temps écoulé=", t2-t1)
    A = 0
    B = 100000
    mesure_perf = False

    if mesure_perf:
        for k in range(1, 8):
            V = unTableau(A, B, 100*2**k)
            temps_d_exécution(tri_insertion, V)
        for k in range(1, 8):
            V = unTableau(A, B, 100*2**k)
            temps_d_exécution(tri_fusion, V)
