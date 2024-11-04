from domino_jeu import * # regroupement des 2 class effectuées des TD 1.1 et TD 1.2

# TD 1.3
class Pioche:
    def __init__(self) -> None:
        a = 0
        test = []
        while a <= 28:
            b = random.randint(0, 6)
            c = random.randint(0, 6)
            a += (b + c)
            test.append(Domino(b, c))
        random.shuffle(test)
        self.jeu = test
    
    def __str__(self) -> str:
        chaine="la pioche : "
        for i in self.jeu:
            chaine += Domino.__str__(i)
        return chaine
    
    def retirer(self) -> list:
        a = self.jeu.pop()
        return a
    
    def est_vide(self) -> bool:
        return len(self.jeu) == 0

# TD 1.4
class Chaine:
    def __init__(self) -> None:
        self.tete = None
        self.queue = None
        self.taille = 0 # = nb pièces
    
    def __str__(self) -> str:
        chaine = ""
        if type(self.tete) != int or type(self.queue) != int:
            chaine=f"\nSon jeu (de taille {self.taille} : {self.tete}|{self.queue})"
        else:
            chaine=f"\n- Tête : {self.tete}\n- Queue : {self.queue}\n- Taille : {self.taille}"
        return chaine
    
    def commence(self, dom: Domino) -> None:
        self.tete = dom.gauche
        self.queue = dom.droite
        self.taille += 1
    
    def ajoute_en_tete(self, dom: Domino) -> None:
        provisoire = f"{self.tete}|{str(dom)}"
        self.tete = provisoire
        self.taille += 1
    
    def ajoute_en_queue(self, dom: Domino) -> None:
        provisoire = f"{self.queue}|{str(dom)}"
        self.queue = provisoire
        self.taille += 1
    
    def est_vide(self):
        return self.taille == 0

# TD 1.5
class Jeu_Domino:
    def __init__(self, name1: str, name2: str) -> None:
        self.joueurs = [Joueur(name1), Joueur(name2)]
        self.pioche = [Pioche(), Pioche()]
        self.chaine = [Chaine(), Chaine()]
    
    def affiche(self):
        for i in range(len(self.joueurs)):
            chaine = f"👇 Voici {self.joueurs[i]}\n"
            print(chaine)
    
    def distribuer(self, nb_joueurs):
        """
        construit le jeu de chaque joueur en prélevant chaque pièce dans la pioche.
        """
        for i in range(nb_joueurs):
            self.joueurs[i].jeu = self.pioche[i].jeu

if __name__ == "__main__":
    print("Création de 2 joueurs...")
    LESjoueurs = Jeu_Domino("Donald Trump", "Kamala Harris")
    print("Distribution du jeu...")
    LESjoueurs.distribuer(2)
    print("Les joueurs :\n")
    LESjoueurs.affiche()

