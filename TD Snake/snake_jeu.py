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
PERIODE_RAFF_MS = 100


def jouer():
    spg.fenetre_init(DIM_X, DIM_Y, H_SCORE_EN_PXL, CASE_EN_PIXEL)

    on_joue = True

    while on_joue:
        spg.maj_evts_souris_clavier()
        # renvoie le couple des deplacements (horizontal et vertical)
        vitesse = spg.mouvement(False)
        if not vitesse == (0, 0):
            print(vitesse)
        spg.attente(PERIODE_RAFF_MS - 10*LEVEL)
        if spg.sortie():
            on_joue = False
    spg.attente(5000)
    spg.fin()


jouer()
