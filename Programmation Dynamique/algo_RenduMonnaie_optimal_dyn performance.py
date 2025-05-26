import timeit
import functools
from fibo import fibo_dyn, fibo_memo, fibo_rec
from algo_RenduMonnaie_optimal_dyn import euros
from algo_chemins import chemin, chemins_memo, chemins_dyn


def temps_d_execution(f, x):
    """mesure le temps d'exeution de f(x)"""
    print("{} avec timeit et x={}".format(f, x))
    print(timeit.timeit(functools.partial(f, x), number=10))


def temps_d_execution_2(f, x, y):
    """mesure le temps d'execution de f(x)"""
    print("{} avec timeit et x={} et y={}".format(f, x, y))
    print(timeit.timeit(functools.partial(f, x, y), number=1))


print(euros == (1, 2, 5, 20, 50, 100))
a_rendre = 29
n = 25
i = 3
j = 4
# temps_d_execution_2(nb_rendu, euros, a_rendre)
# temps_d_execution_2(nb_rendu_memo, euros, a_rendre)
# temps_d_execution_2(nb_rendu_dyn, euros, a_rendre)
temps_d_execution(fibo_rec, n)
temps_d_execution(fibo_memo, n)
temps_d_execution(fibo_dyn, n)
temps_d_execution_2(chemin, i, j)
temps_d_execution_2(chemins_memo, i, j)
temps_d_execution_2(chemins_dyn, i, j)
