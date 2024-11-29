import snake_pygame as spg
from snake_classes import *
from random import randint

LEVEL=1
# dimensions de la fenêtre DIM_X (en pxl)* DIM_Y(en pxl) + taille score (en pxl)  )

DIM_X, DIM_Y = 40, 30            # nombre de cases (point) en x et en y dans la fenetre
H_SCORE_EN_PXL = 40              # hauteur du panneau de score en pixels
CASE_EN_PIXEL = Point.taille_pxl # taille d'une case (unite de longueur du snake)

COLOR_SNAKE_0= (19, 244, 234)    # bleu lagon
PERIODE_RAFF_MS=100



def jouer():
    spg.fenetre_init(DIM_X, DIM_Y,H_SCORE_EN_PXL,CASE_EN_PIXEL)

    on_joue = True

    while on_joue :
        spg.maj_evts_souris_clavier()
        vitesse=spg.mouvement(False ) # renvoie le couple des deplacements (horizontal et vertical)
        if not vitesse == (0,0) : print(vitesse)
        spg.attente( PERIODE_RAFF_MS - 10*LEVEL )
        if spg.sortie() : on_joue = False
    spg.attente( 5000 )
    spg.fin()

jouer()