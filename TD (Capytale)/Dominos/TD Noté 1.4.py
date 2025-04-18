# regroupement des 2 class effectuées des les 2 derniers TD
from domino_jeu import Domino


class Chaine:
    def __init__(self) -> None:
        self.tete = None
        self.queue = None
        self.taille = 0  # = nb pièces

    def __str__(self) -> str:
        chaine = ""
        if type(self.tete) is not int or type(self.queue) is not int:
            chaine = (
                "\n"
                f"Son jeu (de taille {self.taille} : {self.tete}|{self.queue})"
            )
        else:
            chaine = (
                "\n"
                f"- Tête : {self.tete}\n"
                f"- Queue : {self.queue}\n"
                f"- Taille : {self.taille}"
            )
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


if __name__ == "__main__":
    Kylianlebg = Chaine()
    print("Bienvenue Kylian_le_bg !")
    print("Kylian_le_bg est-t-il vide ? ->", Kylianlebg.est_vide(), "\n")
    Ajout1 = Domino(5, 6)
    Kylianlebg.commence(Ajout1)
    print("Kylian_le_bg a commencé son jeu !")
    print("👇 Voici Kylian_le_bg :", str(Kylianlebg))
    print("Kylian_le_bg est-t-il vide ? ->", Kylianlebg.est_vide(), "\n")
    Ajout2 = Domino(2, 3)
    Kylianlebg.ajoute_en_tete(Ajout2)
    print("Kylian_le_bg a ajouté un domino à la tête des dominos !")
    Ajout3 = Domino(4, 1)
    Kylianlebg.ajoute_en_queue(Ajout3)
    print("Kylian_le_bg a ajouté un domino à la queue des dominos !\n")
    print("👇 Voici Kylian_le_bg :", str(Kylianlebg))
    print("Kylian_le_bg est-t-il vide ? ->", Kylianlebg.est_vide())
