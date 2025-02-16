def nombre_de_mots(phrase: str):
    # Façon TBpM (rapide)
    # if (phrase[-1] == "!" or phrase[-1] == "?"):
    #     return len(phrase.split(" ")) - 1
    # return len(phrase.split(" "))

    # Autre façon (lente)
    nbMots = 1
    pList = list(phrase)
    for elm in range(len(pList)):
        if (
            pList[elm] == " " and
            pList[elm + 1] != "?" and
            pList[elm + 1] != "!"
        ):
            nbMots += 1
    return nbMots


assert nombre_de_mots('Cet exercice est simple.') == 4
assert nombre_de_mots('Le point d exclamation est séparé !') == 6
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10
assert nombre_de_mots('Fin.') == 1


class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche: None | Noeud = None
        self.droit: None | Noeud = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche is not None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        else:
            if self.droit is not None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
assert arbre.gauche.etiquette == 3
assert arbre.droit.etiquette == 9
assert arbre.gauche.gauche.etiquette == 1
assert arbre.gauche.droit.etiquette == 6
