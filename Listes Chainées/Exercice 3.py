class Maillon:
    def __init__(self, v: any, s: any) -> None:
        self._valeur = v
        self._suivant = s

    # retourne la valeur du maillon
    def valeur(self) -> any:
        return self._valeur

    # retourne la queue de la liste
    def suite(self) -> any:
        return self._suivant

    # methode de classe (partagée par toutes les instances)
    def est_vide(lst) -> bool:
        return lst is None


def taille_iter(L: Maillon) -> int:
    a: int = 1
    maillon: Maillon | None = L.suite()
    while maillon:
        a += 1
        print(maillon.valeur())
        maillon = maillon.suite()
    return a


def taille_rec(lst: Maillon) -> int:
    if lst == None:
        return 0
    print(lst.valeur())
    return taille_rec(lst.suite()) + 1


m = Maillon(9, None)
L1 = m

m1 = Maillon(6, m)
L2 = m1

m2 = Maillon(3, m1)
L3 = m2

L4 = Maillon(30, Maillon(44, Maillon(50, None)))
print(taille_iter(L4))
print(taille_rec(L4))
