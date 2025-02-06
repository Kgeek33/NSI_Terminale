import csv
from TD_Villes_classe_ville import Ville


class Abr_ville:
    def __init__(self, v: Ville, g=None, d=None):
        """ prend en paramètre
        v l'instance de la classe Ville correspondant à une ligne de ville
        extraite du fichier, g un arbre gauche et
        d un arbre droit"""
        self._ville = v
        self._gauche = g
        self._droit = d

    def __str__(self):
        return str(self._ville.affiche_nom())

    def gauche(self):
        return self._gauche

    def droit(self):
        return self._droit

    def valeur(self):
        return self._ville

    def inserer(self, v: Ville):
        if self is None:
            self = Abr_ville(v, None, None)
        else:
            if v.get_rang() < self._ville.get_rang():
                if self._gauche is None:
                    self._gauche = Abr_ville(v, None, None)
                else:
                    self._gauche.inserer(v)
            else:
                if self._droit is None:
                    self._droit = Abr_ville(v, None, None)
                else:
                    self._droit.inserer(v)

    def recherche(self, rg: int):
        if self is None:
            return None
        if rg == self._ville.get_rang():
            return self
        if rg < self._ville.get_rang():
            return self.gauche().recherche(rg)
        return self.droit().recherche(rg)


def parcours_infixe2(self: Ville):
    if self is None:
        return ""
    return (
        parcours_infixe2(self.gauche()) +
        self.__str__() + "\n" +
        parcours_infixe2(self.droit())
    )


liste_villes = []
with open("Arbres/villes.csv", "r", encoding="UTF-8") as fichier:
    lecteur = csv.reader(fichier, delimiter=",")
    for ligne in lecteur:
        liste_villes.append(ligne)

for villes in liste_villes:
    if Ville(villes).rang == 100:
        ville_racine = Ville(villes)
        villesClass = Abr_ville(Ville(villes))

for LAville in liste_villes:
    UNEclass = Ville(LAville)
    if UNEclass.rang != ville_racine.rang:
        villesClass.inserer(UNEclass)
        print(villesClass.gauche())
        print(villesClass.droit())

print(villesClass)
print(parcours_infixe2(villesClass))
print(villesClass.recherche(100))
print(villesClass.recherche(200))
print(villesClass.recherche(3))
print(villesClass.recherche(1))
