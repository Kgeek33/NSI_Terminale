from random import randint
import snake_pygame as spg

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (89, 27, 219)


class Point:
    # attribut de classe : définit
    # la taille d'un point (taille du côté) en pixels
    taille_pxl = 20

    def __init__(
            self,
            x_m: int,
            y_m: int,
            x: int,
            y: int,
            c: tuple[int]
            ) -> None:
        """x_m et y_m (entiers) definissent le max en x et en y,
        x et y (entiers) les coordonnées du point et
        c (tuple RGB) sa couleur """
        self.x_max = x_m
        self.y_max = y_m
        self.abs = max(min(x, self.x_max), 0)
        self.ord = max(min(y, self.y_max), 0)
        self.couleur = c

    def __str__(self) -> str:
        """renvoie une chaine sous la forme '(x,y)'"""
        return f"({self.x_max},{self.y_max})"

    def __eq__(self, p):
        """deux points sont egaux ssi
        ils ont les memes coordonnees (couleur indifferente)"""
        return self.abs == p.abs and self.ord == p.ord

    def placer(self) -> None:
        """
        place le point dans le jardin (affichage dans la fenetre graphique)
        """
        spg.affiche_point(self, self.couleur)

    def effacer(self):
        spg.affiche_point(self, spg.COLOR_JARDIN)

    def voisin(self, p):
        """ retourne True si les points self et
        p diffèrent d'une case horzontale ou verticale """
        return "à compléter"


class Pomme:
    bonus_pomme_rouge = 10

    def __init__(self, pt: Point, d: int) -> None:
        """pt est une instance de la classe Point et
        d un entier désignant la durée de vie de la pomme"""
        self.point = pt
        self.duree = d

    def pourrie(self, j: int = 1) -> bool:
        """décompose la pomme et renvoie True si
        la pomme a depassé sa duree de vie, False sinon"""
        self.duree -= j
        return self.duree <= 0

    def jeter(self):
        """fait disparaitre la pomme du jardin"""
        self.point.effacer()

    def placer(self):
        """affiche la pomme dans la fenetre graphique"""
        self.point.placer()

    def __str__(self) -> str:
        return str(self.point) + f" duree : {self.duree}"


class Snake:
    def __init__(self, x_m: int, y_m: int, c: tuple[int]) -> None:
        """x_m et y_m (entiers) definissent le max en x et en y de la zone
        dans laquelle pourra évoluer le serpent, c sa couleur (tuple RGB)"""
        self.x_max = x_m
        self.y_max = y_m
        self.couleur = c
        # la vitesse est la derniÃ¨re vitesse demandÃ©e par le joueur
        # si le joueur relache les fleches de direction
        # le serpent continue sur son Ã©lan
        self.vitesse = (0, 0)
        # le corps est une liste de 1 seul point quelque part dans le jardin
        S = Point(x_m, y_m, randint(0, x_m), randint(0, 2), c)
        self.corps = [S]
        self.afficher()
        # et les autres attributs :
        self.score = 0
        self.vivant = True

    def __len__(self) -> int:
        """renvoie la longueur du serpent"""
        return len(self.corps)

    def __str__(self) -> str:
        ch = f"corps : {len(self)}"
        for LEPLAIZ in self.corps:
            ch += str(LEPLAIZ)
        return ch

    def afficher(self) -> None:
        """affiche le corps du serpent dans la fenêtre"""
        for p in self.corps:
            p.placer()

    def contient(self, x, y) -> bool:
        """renvoie True si les coordonnées x,y sont celles
        d'un point du corps du serpent"""
        for p in self.corps:
            if p.abs == x and p.ord == y:
                return True
        return False

    def get_tete(self) -> Point:
        """renvoie le point de tête"""
        return self.corps[-1]

    def get_queue(self) -> Point:
        """renvoie le point de queue"""
        return self.corps[0]

    def get_corps_sans_tete(self) -> list[Point]:
        """renvoie la liste des points sans la tête"""
        return self.corps[:-1]

    def est_dans_zone(self, x, y) -> bool:
        return x >= 0 and x <= self.x_max and y >= 0 and y <= self.y_max

    def grandir_en_tete(self):
        """fait grandir le corps par la tête dans
        le sens de deplacement courant"""
        t = self.get_tete()
        nx = t.abs + self.vitesse[0]
        ny = t.ord + self.vitesse[1]
        if self.est_dans_zone(nx, ny) and not self.contient(nx, ny):
            t = Point(self.x_max, self.y_max, nx, ny, self.couleur)
            self.corps.append(t)
            t.placer()
        else:
            self.vivant = False

    def avale(self, pomme: Pomme) -> None | AssertionError:
        """pomme est une instance de Pomme.
        fait grandir le corps par le haut (la tête) dans le sens
        de deplacement courant"""
        assert self.get_tete() == pomme.point
        print("mange ", str(pomme))
        self.grandir_en_tete()

    def peut_manger(self, pomme: Pomme) -> bool:
        """pomme est une instance de Pomme
        renvoie True si la tête est sur la pomme"""
        t = self.get_tete()
        return t == pomme.point

    def se_deplace(self, vitesse) -> None:
        """ deplace le serpent dans le sens de
        la vitesse (couple (Vx,Vy) passée en parametre)

        maintient un attribut *vivant* comme suit
        le serpent ne reste vivant que
        * si le deplacement le maintient dans les limites du jardin
        * si le deplacement n'est pas un retournenemnt
        """
        self.vitesse = vitesse
        self.grandir_en_tete()

        q = self.corps.pop(0)
        q.effacer()

    def est_vivant(self):
        """renvoie True si le serpent bouge encore dans le jeu, False sinon """
        return self.vivant

    def se_mord_la_queue(self) -> bool:
        """ renvoie True et tue le serpent si
        la tete coincide avec une autre partie du corps"""
        if self.get_tete() in self.get_corps_sans_tete():
            self.vivant = False
            return True
        return False


# les tests du module
if __name__ == '__main__':
    # nombre de cases (point) en x et en y dans la fenetre
    DIM_X, DIM_Y = 40, 30
    H_SCORE_EN_PXL = 40  # hauteur du panneau de score en pixels
    spg.fenetre_init(DIM_X, DIM_Y, H_SCORE_EN_PXL, Point.taille_pxl)

    # tests de la classe Point
    point_A = Point(20, 10, 2, 3, BLUE)
    print(str(point_A))
    point_A.placer()
    point_B = Point(20, 10, 25, -3, GREEN)
    print(str(point_B))
    point_B.placer()
    L_COLORS = [BLACK, YELLOW, RED, PURPLE]
    for k in range(4):
        point_B = Point(20, 10, 25, -3, L_COLORS[randint(1, len(L_COLORS))-1])
        print(str(point_B))
        point_B.placer()
        spg.attente(200)
        point_B.effacer()

    # tests de la classe Pomme
    # a completer

    # tests de la classe Snake
    mon_snake = Snake(DIM_X, DIM_Y, (19, 244, 234))
    print(str(mon_snake))
    mon_snake.se_deplace((0, 1))

    def ligne_droite(n, vit):
        global mon_snake
        for k in range(n):
            mon_snake.se_deplace(vit)
            # if k % 3 == 0:
            #     pt_tete = mon_snake.get_tete()
            #     pomme = Pomme(pt_tete, 100)
            #     mon_snake.avale(pomme)
            spg.score(0, mon_snake.y_max, Point.taille_pxl, 1000+k, WHITE)
            spg.attente(500)

    ligne_droite(DIM_Y//3, (0, 1))
    ligne_droite(3, (-1, 0))
    ligne_droite(DIM_Y//3, (0, -1))
    ligne_droite(2, (-1, 0))

    spg.attente(5000)
    spg.fin()
