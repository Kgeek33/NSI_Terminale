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


def renverser(lst):
    """renvoie une nouvelle liste inversion de la liste lst
    renverser (None) renvoie  None
    renverser [30] renvoie   [30]
    renverser [3, 6, 9, 100] renvoie  [100, 9, 6, 3]
    """
    maillon = lst  # adresse du premier maillon de la liste
    rev_lst = None    # liste vide
    while maillon is not None:
        rev_lst = Maillon(maillon._valeur, rev_lst)
        maillon = maillon.suite()
        # ou bien maillon = maillon._suivant
    return rev_lst


m = Maillon(9, None)
L1 = m

m1 = Maillon(6, m)
L2 = m1

m2 = Maillon(3, m1)
L3 = m2

L4 = Maillon(30, Maillon(44, Maillon(30, None)))

L3 = renverser(None)
print(str(None), "renversée : ", str(L3))
L3 = renverser(L1)
print(str(L1), "renversée : ", str(L3))
L3 = renverser(L2)
print(str(L2), "renversée : ", str(L3))
