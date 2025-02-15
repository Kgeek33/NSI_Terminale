def insertion_abr(a, cle):
    if cle < a[1]:
        if a[0] is None:
            a0 = (None, cle, None)
            return (a0, a[1], a[2])
        return (insertion_abr(a[0], cle), a[1], a[2])

    if cle > a[1]:
        if a[2] is None:
            a2 = (None, cle, None)
            return (a[0], a[1], a2)
        return (a[0], a[1], insertion_abr(a[2], cle))
    return a


n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

assert insertion_abr(abr1, 4) == ((None, 0, None), 1,
                                  (None, 2, (None, 3, (None, 4, None))))
assert insertion_abr(abr1, -5) == (((None, -5, None), 0,
                                    None), 1, (None, 2, (None, 3, None)))
assert insertion_abr(abr1, 2) == (
    (None, 0, None), 1, (None, 2, (None, 3, None)))


def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    n = len(liste_masses)
    nb_boites = 0
    boites = [0 for _ in range(n)]
    for masse in ...:
        i = 0
        while i < nb_boites and boites[i] + ... > c:
            i = i + 1
        if i == nb_boites:
            ...
        boites[i] = ...
    return ...
