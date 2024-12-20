import snake_pygame as spg
from snake_classes import *
from random import randint

LEVEL = 1
# dimensions de la fenêtre DIM_X (en pxl)* DIM_Y(en pxl) + taille score (en pxl)  )

# nombre de cases (point) en x et en y dans la fenetre
DIM_X, DIM_Y = 40, 30
H_SCORE_EN_PXL = 40              # hauteur du panneau de score en pixels
# taille d'une case (unite de longueur du snake)
CASE_EN_PIXEL = Point.taille_pxl

COLOR_SNAKE_0 = (19, 244, 234)    # bleu lagon
L_COLORS = [BLACK, YELLOW, RED, PURPLE]


def jouer():
    PERIODE_RAFF_MSs = 99
    spg.fenetre_init(DIM_X, DIM_Y, H_SCORE_EN_PXL, CASE_EN_PIXEL)

    snake = Snake(DIM_X, DIM_Y, COLOR_SNAKE_0)
    vitesse = (0, 0)
    on_joue = True
    snake.afficher()

    DEScoor = Point(20, 10, randint(0, H_SCORE_EN_PXL - 10),
                    randint(0, H_SCORE_EN_PXL - 10), RED)
    LApomme = Pomme(DEScoor, 5)
    LApomme.placer()

    LEscore = 0
    spg.score(0, snake.y_max, Point.taille_pxl, LEscore, WHITE)

    while on_joue:
        spg.maj_evts_souris_clavier()
        # renvoie le couple des deplacements (horizontal et vertical)
        v = spg.mouvement(False)

        if snake.contient(LApomme.point.abs, LApomme.point.ord):
            if snake.get_tete() == LApomme.point:
                snake.avale(LApomme)
                LEscore += 1
                spg.score(0, snake.y_max, Point.taille_pxl, LEscore, WHITE)
            DEScoor = Point(20, 10, randint(0, H_SCORE_EN_PXL - 10), randint(0,
                            H_SCORE_EN_PXL - 10), L_COLORS[randint(1, len(L_COLORS))-1])
            LApomme = Pomme(DEScoor, 5)
            LApomme.placer()
        if LApomme.pourrie(0.5):
            LApomme.jeter()
            DEScoor = Point(20, 10, randint(0, H_SCORE_EN_PXL - 10), randint(0,
                            H_SCORE_EN_PXL - 10), L_COLORS[randint(1, len(L_COLORS))-1])
            LApomme = Pomme(DEScoor, 5)
            LApomme.placer()

        if v != (0, 0):
            vitesse = v

        if not vitesse == (0, 0):
            snake.se_deplace(vitesse)

        if spg.sortie() or not snake.est_vivant():
            on_joue = False
        else:
            spg.attente(PERIODE_RAFF_MSs - 10*LEVEL)

    spg.fin()
    if not snake.est_vivant():
        print("Snake is dead!")


jouer()
