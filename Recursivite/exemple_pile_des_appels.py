"""visualiser l'arbre des appels et les états successifs de la pile"""


# 0 visu pile d'appels
def g(x):
    w = x*x
    return w


z = g(5)
u = g(10)
t = g(z)
u = g(u)

le_resultat = z+u+t


# 1 visu pile d'appels
def g(x, y):
    w = x*y
    return 100+w


def f(x, y):
    z = x+y
    u = g(x-1, y*2)
    return z+u


le_resultat = f(1, 5)


# 2 visu pile d'appels
def g(x, y):
    w = x*y
    return 100+w


def f(x, y):
    z = x+y
    u = g(x-1, y*2)
    # appel suppémentaire au même niveau
    u = g(x, u)
    return z+u


le_resultat = f(1, 5)


# 3 visu pile d'appels
def g(x, y):
    w = x*y
    return 100+w


def f(x, y):
    z = x+y
    u = z-1
    for i in range(4):
        u = g(x, u)
    return z+u


le_resultat = f(1, 5)


# 4 visu pile d'appels
def f(x):
    z = x*x
    return z-x


def g(y):
    x = y+1
    t = f(x)
    y = f(y)
    return t+y+x


le_resultat = g(4)


# 5 visu pile d'appels
def f(x):
    z = x*x
    return z-x


def g(y):
    x = y+1
    t = f(x)
    return t+y+x


def h(x):
    z0 = g(x+1)
    z1 = g(x)
    z = z0*z1
    return z-x


le_resultat = h(4)
