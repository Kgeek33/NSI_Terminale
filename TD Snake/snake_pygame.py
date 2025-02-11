#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module pygame pour SNAKE
"""

import pygame
from pygame.locals import Rect

COLOR_JARDIN = (29, 108, 5)  # vert pelouse
# screen est la fenêtre pygame
screen = None
# event et keys sont les événements et les touches clavier appuyées
# les variables sont mises à jour par la fonction miseAJourActions()
event, keys = None, None


def fenetre_init(dim_x, dim_y, score_en_pxl, case_en_pxl) -> None:
    """
    entrée :dim_x,dim_y le nombre de points en x, et en y,
    score_en_pxl la hauteur du panneau de score en pixels,
    et case_en_pxl la taille d'un point en pixel
    sortie : -
    creation de la fenetre graphique
    """
    global screen
    # dimensions de la fenêtre DIMX (en pxl)* DIMY(en pxl) +
    # taille score (en pxl)  )
    pygame.init()
    r_fenetre = Rect(0, 0, (dim_x+1)*case_en_pxl,
                     (dim_y+1)*case_en_pxl+score_en_pxl)
    screen = pygame.display.set_mode(r_fenetre.size, 0)
    # titre de la fenetre (bandeau blanc supérieur)
    pygame.display.set_caption("Snake!")
    screen.fill(COLOR_JARDIN)
    # ligne frontière avant le bandeau des scores
    pygame.draw.line(screen, (255, 255, 255), (0, (dim_y+1)*case_en_pxl),
                     ((dim_x+1)*case_en_pxl, (dim_y+1)*case_en_pxl))
    pygame.display.flip()  # Mise à jour de l'affichage complet


def attente(delai_ms: int) -> None:
    """
    entrée : delai_ms nombre de millisecondes
    sortie : -
    attend delai_ms millisecondes, attente blocante.
    """
    pygame.time.wait(delai_ms)


def sortie() -> bool:
    """
    entrée : -
    sortie : booléen
    renvoie True si le joueur ferme la fenêtre ou appuie sur la touche Echap,
    False sinon
    """
    global event, keys
    if event.type == pygame.QUIT:
        print("close!")
        return True
    if keys[pygame.K_ESCAPE]:
        print("escape!")
        return True
    return False


def fin() -> None:
    """
    entrée : -
    sortie : -
    appel la fonction pygame.quit()
    """
    pygame.quit()


def maj_evts_souris_clavier() -> None:
    """
    entrée : -
    sortie : -
    mise à jour des variables event & keys du module décrivant
    les evenements souris et clavier
    """
    global event, keys
    # pour obtenir un seul événement de la file d'attente.
    event = pygame.event.poll()
    # pour obtenir une liste de l'état de toutes les clés.
    # La liste contient 0 pour toutes les touches qui ne sont pas enfoncées
    # et 1 pour toutes les touches sur lesquelles vous appuyez.
    # Son index dans la liste est défini par
    # des constantes dans le module pygame,
    # toutes préfixées par K_ et le nom de la clé.
    keys = pygame.key.get_pressed()


def mouvement(debug=False):
    """
    entrée : debug, un booléeen, autorisant ou non
    l'affichage de l'interprétation des flèches
    sortie : le couple (deplacement horizontal (+1 ou -1),
    deplacement vertical (+1 ou -1))
    interprète les fleches enfoncées sous forme
    de deplacements attendus du serpent
    """
    global keys
    if keys[pygame.K_RIGHT]:
        if debug:
            print("right")
        return (1, 0)
    elif keys[pygame.K_UP]:
        if debug:
            print("up")
        return (0, -1)
    elif keys[pygame.K_LEFT]:
        if debug:
            print("left")
        return (-1, 0)
    elif keys[pygame.K_DOWN]:
        if debug:
            print("down")
        return (0, 1)
    return (0, 0)


def affiche_point(p, color):
    """
    entrée : p un Point, color une couleur en RGB (par défaut bleu)
    sortie : -
    colore un carré de la taille p.taille_pxl (en pixels) de couleur color
    aux coordonnées du point p, puis l'affiche
    """
    global screen
    rect = Rect(p.taille_pxl*p.abs, p.taille_pxl *
                p.ord, p.taille_pxl, p.taille_pxl)
    pygame.draw.rect(screen, color, rect)
    pygame.display.flip()  # Mise à jour de l'affichage complet


def score(pos_x, pos_y, case_en_pxl, s, color):
    """
    entrée : pos_x,pos_y les coordonnées de la position en haut à gauche
    du bandeau de score,
    case_en_pxl la taille d'une case en pixels,
    s un entier désignant le score à afficher, color une couleur en RGB
    désignant la couleur de l'affichage
    sortie : -
    affiche le score s dans le bandeau défini par pos_x,pos_y
    """
    global screen
    # on definit la police et la taille
    police = pygame.font.SysFont("consolas", 30)
    chaine_score = "Score : {}".format(s)
    # imageTxt contient le msg
    image_txt = police.render(chaine_score, True, color, COLOR_JARDIN)
    screen.blit(image_txt, ((pos_x+1)*case_en_pxl, (pos_y+1)*case_en_pxl+1))

# fin du fichier snake_pygame.py
