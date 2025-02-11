import random
from domino import Domino
from domino_joueur import Joueur

max_domino = 6


class Pioche:
    def __init__(self) -> None:
        self.jeu = []

    def __str__(self) -> str:
        chaine = "la pioche : "
        random.shuffle(self.jeu)
        for i in self.jeu:
            chaine += Domino.__str__(i)
        return chaine

    def retirer(self) -> list:
        a = self.jeu.pop()
        return a

    def est_vide(self) -> bool:
        return len(self.jeu) == 0


def nb_pieces_par_joueur(nb):
    # pour deux joueurs  : 7 dominos à chacun, le reste constituera la pioche
    if nb == 2:
        return 7
    # pour trois ou quatre joueurs  : 6 dominos à chacun
    # le reste constituera la pioche
    elif nb <= 4:
        return 6
    else:
        return 28//nb


if __name__ == '__main__':
    dom_par_personnes = nb_pieces_par_joueur(3)
    florent = Pioche()
    lucas = Pioche()
    raphael = Pioche()
    print("Voici Florent -> ", str(florent))
    print("Voici Lucas -> ", str(lucas))
    print("Voici Raphaël -> ", str(raphael))
    a = Domino(random.randint(0, max_domino), random.randint(0, max_domino))
    b = Domino(random.randint(0, max_domino), random.randint(0, max_domino))
    c = Domino(random.randint(0, max_domino), random.randint(0, max_domino))
    Joueur.recevoir(florent, a)
    Joueur.recevoir(florent, b)
    Joueur.recevoir(lucas, c)
    Joueur.recevoir(lucas, a)
    Joueur.recevoir(raphael, b)
    Joueur.recevoir(raphael, c)
    print("\nFlorent a désormais -> ", str(florent))
    print("Lucas a désormais -> ", str(lucas))
    print("Raphaël a désormais -> ", str(raphael))
    Joueur.extraire(florent, a)
    Joueur.extraire(lucas, c)
    Joueur.extraire(lucas, a)
    Joueur.extraire(raphael, c)
    print("\nEst-ce que Florent a terminé son jeu ? ->", florent.est_vide())
    print("Est-ce que Lucas a terminé son jeu ? ->", lucas.est_vide())
    print("Est-ce que Raphaël a terminé son jeu ? ->", raphael.est_vide())
    print("Florent a finalement ->", str(florent))
    print("Lucas a finalement ->", str(lucas))
    print("Raphaël a finalement ->", str(raphael))
