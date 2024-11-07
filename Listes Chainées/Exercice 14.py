class Maillon:
    def __init__(self, v: any, s: any) -> None:
        self._valeur = v
        self._suivant = s

    def __str__(self, chaine="|"):
        "__str__() n'attend pas une liste vide"
        if Maillon.est_vide(self._suivant):
            return chaine+str(self._valeur)+"|"
        else:
            return chaine+"{}->{}".format(self.valeur(), Maillon.__str__(self.suite(), ""))

    # retourne la valeur du maillon
    def valeur(self) -> any:
        return self._valeur

    # retourne la queue de la liste
    def suite(self) -> any:
        return self._suivant

    # methode de classe (partagée par toutes les instances)
    def est_vide(lst) -> bool:
        return lst == None


def taille_iter(L: Maillon) -> int:
    a: int = 1
    maillon: Maillon | None = L.suite()
    while maillon:
        a += 1
        print(maillon.valeur())
        maillon = maillon.suite()
    return a


def identiques(lst1: Maillon, lst2: Maillon) -> bool:
    """
    retourne un booléen précisant si les listes lst1 et lst2 contiennent les mêmes éléments dans le même ordre
    """
    for _ in range(taille_iter(lst1)):
        if lst1.valeur() != lst2.valeur():
            return False

        lst1 = lst1.suite()
        lst2 = lst2.suite()
    return True


m = Maillon(9, None)
L1 = m

m1 = Maillon(6, m)
L2 = m1

m2 = Maillon(3, m1)
L3 = m2

L4 = Maillon(30, Maillon(44, Maillon(30, None)))

print(identiques(L4, L3))
print(identiques(L4, L4))
