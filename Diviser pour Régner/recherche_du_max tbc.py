
#  version diviser pour regner
def diviser(lst):
    """
    prend une liste lst
    renvoie deux listes correspondant à la moitié droite et à la moitié gauche
    """
    milieu = len(lst)//2
    return lst[:milieu], lst[milieu:]


def maximum_dpr(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    left, right = diviser(lst)
    max_left = maximum_dpr(left)
    max_right = maximum_dpr(right)

    return max_left if max_left > max_right else max_right


#  version diviser pour regner rapide (sans copie de listes)
def diviser_rapide(lst, debut, fin):
    """prend une liste lst, les indices de debut et de fin et
    renvoie l'indice frontière entre la moitié droite et à la moitié gauche"""
    pass


def maximum_dpr_rapide(lst, debut=0, fin=-1):
    #    print(debut,fin)
    pass
    return "a completer"


# version balayage
def maximum_balayage(lst):
    pass
    return "a completer"


if __name__ == '__main__':

    print("test du maximum")

    vrac = [3, 4, 6, 2, 5, 1, 8, 7]
    print("en vrac :", vrac)
    maxi = maximum_dpr(vrac)
    print("max :", maxi)
#    assert maxi==maximum_balayage(vrac)
    maxi_rapide = maximum_dpr_rapide(vrac)
    print("max rapide :", maxi_rapide)
#    assert maxi_rapide==maximum_balayage(vrac)

    vrac = [30, 4, 26, 28, 15, 12, 80, 71, 54]
    print("en vrac :", vrac)
    maxi = maximum_dpr(vrac)
    print("max :", maxi)
#    assert maxi==maximum_balayage(vrac)
    maxi_rapide = maximum_dpr_rapide(vrac)
    print("max rapide :", maxi_rapide)
#    assert maxi_rapide==maximum_balayage(vrac)


# tests de performance
    mesure_perfs = False

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

    def temps_d_exécution(f, x):
        print("perf_counter de {} avec  n={}".format(f, len(x)))
        t1 = perf_counter()
        r = f(x)
        t2 = perf_counter()
        print("resultat=", r)
        print("temps écoulé=", t2-t1)

    A = 0
    N = 1000000
    B = A+N*10

    if mesure_perfs:
        for k in range(8):
            V = unTableau(A, B, 10**k)
            temps_d_exécution(maximum_balayage, V)
        for k in range(8):
            V = unTableau(A, B, 10**k)
            temps_d_exécution(maximum_dpr, V)
        for k in range(8):
            V = unTableau(A, B, 10**k)
            temps_d_exécution(maximum_dpr_rapide, V)
