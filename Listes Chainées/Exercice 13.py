class Maillon:
    def __init__(self, v: any, s: any) -> None:
        self._valeur = v
        self._suivant = s

    def __str__(self, chaine="|"):
        "__str__() n'attend pas une liste vide"
        if Maillon.est_vide(self._suivant):
            return chaine+str(self._valeur)+"|"
        else:
            return chaine+"{}->{}".format(
                self.valeur(),
                Maillon.__str__(self.suite(), "")
            )

    # retourne la valeur du maillon
    def valeur(self) -> any:
        return self._valeur

    # retourne la queue de la liste
    def suite(self) -> any:
        return self._suivant

    # methode de classe (partagée par toutes les instances)
    def est_vide(lst) -> bool:
        return lst is None


def occurences_iter(x: any, lst: Maillon) -> int:
    a = 0
    while lst is not None:
        if lst.valeur() == x:
            a += 1
        lst = lst.suite()

    return None if a == 0 else a


def occurences_rec(x: any, lst: Maillon) -> int:
    s = 0
    if lst is None:
        return 0
    elif lst.valeur() == x:
        s += 1

    return occurences_rec(x, lst.suite()) + s


m = Maillon(9, None)
L1 = m

m1 = Maillon(6, m)
L2 = m1

m2 = Maillon(3, m1)
L3 = m2

L4 = Maillon(30, Maillon(44, Maillon(30, None)))


print(occurences_iter(30, L4))
print(occurences_rec(30, L4))
