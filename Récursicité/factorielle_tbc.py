from random import randint


def factorielle_rec(n):
    """factorielle récursive"""
    res = 1
    # instruction suivante à remplacer par un code approprié
    if n > 1:
        prec = factorielle_rec(n-1)
        res = n * prec
    return res


def factorielle_iter(n):
    """factorielle itérative"""
    res = 1
    # instruction suivante à remplacer par un code approprié
    for i in range(1, n+1):
        res *= i
    return res


# tests
le_resutat_rec = factorielle_rec(5)
le_resutat_iter = factorielle_iter(5)
print("factorielle recursif de 5 renvoie", le_resutat_rec,
      ", factorielle iteratif de 5 renvoie", le_resutat_iter)
assert le_resutat_rec == le_resutat_iter

# 2 timeit


def genere_tab(N, max):
    """retourne une liste de N entiers compris entre 0 et max"""
    L = []
    # instruction suivante à remplacer par un code approprié
    for _ in range(N):
        L.append(randint(0, max))
    return L

# print(genere_tab(15, 100))
# print(genere_tab(10000000, 1000))


def test(fc_factorielle, j_t):
    """pour tester la fonction passee en paramètre
    (qui pourra être l'une des deux versions récursive ou itérative"""
    for n in j_t:
        k = fc_factorielle(n)
        print("factorielle de ", n, "renvoie", k)


jeu_test = genere_tab(10, 20)
print("jeu de test :", jeu_test)
print("test en recursif")
test(factorielle_rec, jeu_test)
print("test en iteratif")
test(factorielle_iter, jeu_test)

# import timeit, functools
# print("bench factorielle imperative :",
#    timeit.timeit(functools.partial(test,factorielle_iter,jeu_test),number=10))
#
# print("bench factorielle recursive :",
# timeit.timeit(functools.partial(test,factorielle_rec,jeu_test),number=10))

# print(
#   "bench factorielle imperative :",
#   timeit.timeit(functools.partial(factorielle_iter,900),number=1000)
# )
# print(
#   "bench factorielle recursive :",
#   timeit.timeit(functools.partial(factorielle_rec,900),number=1000)
# )
