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


def _(x, lst: Maillon):
    a = None
    while lst.valeur() < x:
        a = Maillon(lst.valeur(), a)
        lst = lst.suite()


def inserer_rec(x: int, lst: Maillon) -> Maillon:
    if lst is None:
        return Maillon(x, None)

    if x <= lst.valeur():
        return Maillon(x, lst)

    return Maillon(lst.valeur(), inserer_rec(x, lst.suite()))


def tri_par_insertion(lst: Maillon) -> Maillon:
    if lst is None:
        return None
    if lst.suite() is None:
        return lst

    return inserer_rec(lst.valeur(), tri_par_insertion(lst.suite()))


m = Maillon(9, None)
L1 = m

m1 = Maillon(6, m)
L2 = m1

m2 = Maillon(3, m1)
L3 = m2

L4 = Maillon(500, Maillon(44, Maillon(30, None)))

print(tri_par_insertion(L4))
