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


def concatener_iter(lst1: Maillon, lst2: Maillon) -> Maillon:
    """
    retourne une nouvelle liste mst3 qui concatène les listes lst1 et lst2
    """
    lst3: Maillon = lst1
    n: int = 0
    m: int = 0
    while lst3.suite() != None:
        lst3 = lst3.suite()
        n += 1
        m += 1
    v = lst3.valeur()
    lst3 = Maillon(v, lst2)
    for _ in range(n, 0, -1):
        lst4: Maillon = lst1
        for _ in range(m-1, -1, -1):
            v = lst4.valeur()
        lst3 = Maillon(v, lst3)
    return str(lst3)


def concatener_rec(lst1: Maillon, lst2: Maillon) -> Maillon:
    if lst1 == None:
        return lst2

    return Maillon(concatener_rec(lst1.valeur(), lst2))


m = Maillon(9, None)
L1 = m

m1 = Maillon(6, m)
L2 = m1

m2 = Maillon(3, m1)
L3 = m2

L4 = Maillon(30, Maillon(44, Maillon(50, None)))

# print(taille_iter(L4))
# print(taille_rec(L4))
# print(nieme_element_iter(2, L4))
# print(nieme_element_rec(2, L4))
