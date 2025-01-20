class Noeud:
    # attribut de classe
    arbre_vide = None

    def __init__(self, v, g, d):
        self._valeur = v
        self._gauche = v
        self._droit = v
    
    def valeur(self):
        return self._valeur
    
    def gauche(self):
        return self._gauche
    
    def droit(self):
        return self._droit
    
    def est_vide(arbre):
        return arbre is Noeud.arbre_vide

