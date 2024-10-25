import random
max_domino=6

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




class Joueur:
    def __init__(self,nom):
        self.nom=nom
        self.jeu=[]
    def __str__(self):
        chaine=f"{self.nom} : "
        for i in self.jeu:
            chaine += Domino.__str__(i)
        somme = self.total()
        chaine += f"---total : {somme}"
        return chaine

    def recevoir(self,dom):
        """dom est une instance de la classe domino
        cette methode ajoute dom au jeu du joueur"""
        self.jeu.append(dom)

    def extraire(self,dom):
        """dom est une instance de la classe domino
        cette methode retire dom au jeu du joueur"""
        if len(self.jeu)==0 :
            return None
        return self.jeu.remove(dom)

    def a_fini(self):
        # renvoie True si le joueur a posé tous ses dominos (son jeu est vide)
        # renvoie False sinon
        return len(self.jeu) == 0

    def convient_avec(self,n):
        # renvoie un domino du jeu avec n à droite ou à gauche
        # renvoie None si aucun domino ne convient
        for i in range(len(self.jeu)):
            if self.jeu[i] == None : print(i, len(self.jeu))
            if self.jeu[i].droit==n or self.jeu[i].gauche==n :
                return self.jeu[i]
        return None

    def tous_la(self,n):
        # renvoie vrai si tous les 7 dominos avec n à droite ou à gauche sont dans le jeu
        cpt=0
        for i in range(len(self.jeu)):
            if self.jeu[i].droit==n or self.jeu[i].gauche==n :
                cpt+=1
            if cpt==max_domino+1 : return True
        return False



    def affiche(self):
        print(self.nom)
        for i in range(len(self.jeu)):
            self.jeu[i].affiche()

    def total(self):
        somme = 0
        for i in self.jeu:
            somme += (i.gauche + i.droite)
        
        return somme

#tests
if __name__ == '__main__' :
    florent = Joueur("Florent")
    lucas = Joueur("Lucas")
    print("Voici", str(florent))
    print("Voici", str(lucas))
    a = Domino(3, 1)
    b = Domino(2, 1)
    c = Domino(3, 6)
    florent.recevoir(a)
    florent.recevoir(b)
    lucas.recevoir(c)
    print("\nDésormais,", str(florent))
    print("Désormais,", str(lucas))
    florent.extraire(a)
    lucas.extraire(c)
    print("\nEst-ce que Florent a terminé son jeu ? ->", florent.a_fini())
    print("Est-ce que Florent a terminé son jeu ? ->", lucas.a_fini())
    print("Finalement,", str(florent))
    print("Finalement,", str(lucas))
