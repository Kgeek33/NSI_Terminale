from arbre_operations import hauteur
from classe_noeud import Noeud
import matplotlib.pyplot as plt

inter_feuilles = 10    # espace horizontal entre deux feuilles


def plot_noeud(v, x, y):
    """ trace un nneud avec sa valeur aux coordonnées x,y du repère"""
    plt.text(x, y, str(v), fontsize=25)


def plot_infixe(A, x, y, decalage):
    """ trace l'arbre en parcours infixe qui démarre en x,y
    on trace le sous arbre gauche décalé horizontalement de -decalage
    et le sous arbre droit décalé de (+decalage)
    La distance verticale entre deux niveaux est de inter_feuilles """

    if True:  # condition à remplacer !
        return
    else:
        # appel récursif sur l'arbre gauche à compléter

        # tracé de ll'arête à compléter   :
        # utiliser plt.plot(
        #   [liste des x des points à joindre],
        #   [liste des y des points à joindre],
        #   'r-',
        #   lw=2 # ligne rouge d'épaisseur 2
        # )

        # tracé du noeud à compléter

        # appel récursif sur l'arbre droit à compléter

        # tracé de ll'arête à compléter   :
        # utiliser plt.plot(
        #   [liste des x des points à joindre],
        #   [liste des y des points à joindre],
        #   'r-',
        #   lw=2 # ligne rouge d'épaisseur 2
        # )
        return


def plot_arbre(A):
    h = hauteur(A)
    # calcul de la fenetre dans laquelle on inscrit l'arbre
    xmin = inter_feuilles
    # espace horizontal entre deux noeuds
    # depend du niveau, initialisé ici pour la racine
    inter_noeud = 2**(h+1)*inter_feuilles
    xmax = xmin+4*inter_noeud
    ymin = inter_feuilles
    # la hauteur de la fenetre dépend de la hauteur de l'arbre
    # l'espacement horizontal entre deux feuilles est aussi
    # l'espacement entre deux niveaux
    ymax = ymin+(h+2)*inter_feuilles
    # fenetre
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)

    # axes = plt.gca()            # objet axes

    # les lignes suivantes sont à décommenter
    # lorsque le debug est terminé (plus besoin du repère pour les réglages)

    # axes.set_frame_on(False) # supprime la boîte carrée
    # qui entoure le graphe, mais pas les graduations (ticks et valeurs).

    # axes.xaxis.set_visible(False) # supprime les ticks et les valeurs
    # sur les axes, en conservant l'axe.

    # axes.yaxis.set_visible(False) # supprime les ticks et les valeurs
    # sur les axes, en conservant l'axe.

    # axes.spines['top'].set_visible(False) # pour enlever le trait supérieur
    # de la boîte entourant le graphe.

    # la racine est positionnnée au milieu en largeur ((xmin+xmax)/2)
    # et legerement plus bas que l ehaut du repère (ymax-inter_feuilles)
    plot_infixe(A, (xmin+xmax)/2, ymax-inter_feuilles, inter_noeud)
    plt.show()


#   tests
A_1 = Noeud('a',
            Noeud('b',
                  Noeud('d', None, None),
                  Noeud('e', None, None)),
            Noeud('c',
                  None,
                  Noeud('f', None, None)))
plot_arbre(A_1)

A_2 = Noeud(1,
            Noeud(2,
                  Noeud(4, Noeud(8, None, None), Noeud(9, None, None)),
                  Noeud(5, Noeud(10, None, None), None)),
            Noeud(3,
                  Noeud(6, None, None), Noeud(7, None, None)))
plot_arbre(A_2)
