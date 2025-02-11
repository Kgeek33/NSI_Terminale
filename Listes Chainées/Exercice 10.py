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


def latestMaillon(lst: Maillon, v) -> Maillon:
    """Cette fonction permet de renvoyer le dernier Maillon"""
    m = Maillon(v, None)
    if lst is None:
        return m
    maillon = lst
    while maillon._suivant is not None:
        maillon = maillon._suivant
    maillon._suivant = m
    return lst
