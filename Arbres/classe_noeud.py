class Noeud:
    # attribut de classe
    arbre_vide = None

    def __init__(self, v, g, d):
        self._valeur = v
        self._gauche = g
        self._droit = d
    
    def valeur(self):
        return self._valeur
    
    def gauche(self):
        return self._gauche
    
    def droit(self):
        return self._droit
    
    def est_vide(arbre):
        return arbre is Noeud.arbre_vide
    

    def est_feuille(self):
        return self.gauche() is Noeud.arbre_vide and self.droit() is Noeud.arbre_vide

A_g = Noeud("D",None,None)
A_1 = Noeud("A",Noeud("B,",None,None),None)
A_2 = Noeud("A",Noeud("B,","D",None),None)
A_3 = Noeud("A",Noeud("B,","D",None),None)
print(A_3.gauche().droit().valeur())