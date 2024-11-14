from  classe_maillon import *

class Pile:
    """structure de pile"""
    def __init__(self):
        #contenu est un maillon
        self.contenu = None

    def est_vide(self):
        return self.contenu is None

    def empiler(self, v):
        """ajoute un maillon dont la valeur est v en tête"""
        #self.contenu=Maillon(v,self.contenu)
        pass

    def depiler(self):
        if (""" a completer """):
            raise IndexError("impossible de depiler une pile vide !!!")
        """ a completer """
        pass


    #permet l'appel str(P) equivalent à P.__str__()
    def __str__(self, chaine="["):
        return str(self.contenu)


P= Pile()
print("pile vide ?", P.est_vide())
P.empiler(5)
print(str(P))
P.empiler(8)
print(str(P))
P.empiler(-2)
print(str(P))
##n=P.depiler()
##print("sommet dépilé =",n)
##print("pile vide ?", P.est_vide())
##print(str(P))


