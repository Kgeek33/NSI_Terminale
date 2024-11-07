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


def trouve_iter(x: any, lst: Maillon):
    k = 0
    while lst != None:
        if x == lst.valeur():
            return k

        lst = lst.suite()
        k += 1
    return None


def trouve_rec(x: any, lst: Maillon):
    if lst == None:
        return None
    if x == lst.valeur():
        return 0
    
    rec = trouve_rec(x, lst.suite())
    if rec == None:
        return None

    return rec + 1


m = Maillon(9, None)
L1 = m

m1 = Maillon(6, m)
L2 = m1

m2 = Maillon(3, m1)
L3 = m2

L4 = Maillon(66, Maillon(44, Maillon(30, None)))

print("30 dans L4 :", trouve_iter(30, L4))
print("20 dans L2 :", trouve_iter(20, L2))
print("30 dans L4 :", trouve_rec(30, L4))
print("20 dans L2 :", trouve_rec(20, L2))
