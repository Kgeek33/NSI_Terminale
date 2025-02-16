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
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                ...
            else:
                self.gauche = ...
        else:
            ...
            ...
            else:
                ... = Noeud(cle)
