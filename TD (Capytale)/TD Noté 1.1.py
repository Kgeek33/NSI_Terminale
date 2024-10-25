import random

class Domino:
    def __init__(self,g,d):
        self.gauche = g
        self.droite = d

    def __str__(self):
        return (f"[{self.gauche}-{self.droite}]")

    def nb_points (self):
        return (self.gauche + self.droite)

    def est_un_double (self):
        return (self.gauche == self.droite)

    def est_un_blanc (self):
        return (self.gauche + self.droite == 0)

#tests
if __name__ == '__main__' :
    # dom est une instance de la classe Domino 
    print(" affichage du 4-1")
    dom=Domino(4, 1)
    print("voici dom -> ", str(dom))
    #test de la methode est_un_double() et de la methode nb_points()
    print("dom est un double ? -> ", dom.est_un_double())
    print("dom est blanc ? -> ", dom.est_un_blanc())
    
    #test de la methode affiche() 
    print(str(dom))
    
    
    # domdom est un double, une autre instance de la classe Domino 
    print("affichage du double 4")
    domdom=Domino(4, 4)
    #test de la methode est_un_double() et de la methode nb_points()
    print("domdom est un double ? -> ", domdom.est_un_double())
    print("domdom est blanc ? -> ", domdom.est_un_blanc())
    
    #test de la methode affiche() 
    print("voici domdom -> ", str(domdom))


