from tkinter import Tk, Canvas
from graphe_dictionnaire_adjacence_tbc import Graphe
# from une_pile_avec_une_liste_chainée import Pile


# Fonctions d'initialisation
def onkeypresse(_):
    """ Cette fonction s'exécute lorsque la touche `r` est cliquée """
    x = 4
    y = 3
    x *= TAILLE_CASE
    y *= TAILLE_CASE
    monCanvas.create_rectangle(
        x,
        y,
        x + TAILLE_CASE,
        y + TAILLE_CASE,
        fill="blue"
    )


def configGraphe(THEgraphe: Graphe):
    """
    Cette fonction configure les sommets et les arrêtes
    à l'initialisation du graphe
    """
    # Ajout des sommets
    for i in range(8):
        for j in range(8):
            THEgraphe.ajouter_sommet((i, j))

    # Ajout des arrêtes des sommets
    THEgraphe.ajouter_arete((0, 0), (0, 1))
    THEgraphe.ajouter_arete((0, 1), (0, 2))
    THEgraphe.ajouter_arete((0, 2), (0, 3))
    THEgraphe.ajouter_arete((0, 3), (1, 3))
    THEgraphe.ajouter_arete((1, 3), (1, 4))
    THEgraphe.ajouter_arete((0, 0), (1, 0))
    THEgraphe.ajouter_arete((1, 0), (2, 0))
    THEgraphe.ajouter_arete((2, 0), (2, 1))
    THEgraphe.ajouter_arete((2, 1), (2, 2))
    THEgraphe.ajouter_arete((2, 2), (3, 2))
    THEgraphe.ajouter_arete((3, 2), (4, 2))
    THEgraphe.ajouter_arete((4, 2), (4, 1))
    THEgraphe.ajouter_arete((4, 1), (4, 0))
    THEgraphe.ajouter_arete((4, 0), (5, 0))
    THEgraphe.ajouter_arete((3, 4), (3, 5))
    THEgraphe.ajouter_arete((3, 5), (3, 6))
    THEgraphe.ajouter_arete((3, 4), (4, 4))
    THEgraphe.ajouter_arete((4, 4), (4, 3))
    THEgraphe.ajouter_arete((4, 3), (5, 3))
    THEgraphe.ajouter_arete((3, 6), (2, 6))
    THEgraphe.ajouter_arete((2, 6), (2, 7))
    THEgraphe.ajouter_arete((2, 6), (1, 6))
    THEgraphe.ajouter_arete((3, 6), (4, 6))
    THEgraphe.ajouter_arete((1, 6), (0, 6))
    THEgraphe.ajouter_arete((0, 6), (0, 7))
    THEgraphe.ajouter_arete((5, 3), (6, 3))
    THEgraphe.ajouter_arete((6, 1), (6, 0))
    THEgraphe.ajouter_arete((6, 1), (7, 1))
    THEgraphe.ajouter_arete((5, 7), (6, 7))
    THEgraphe.ajouter_arete((7, 1), (7, 2))
    THEgraphe.ajouter_arete((7, 4), (7, 5))
    THEgraphe.ajouter_arete((5, 7), (4, 7))
    THEgraphe.ajouter_arete((6, 5), (6, 6))
    THEgraphe.ajouter_arete((6, 5), (5, 5))
    THEgraphe.ajouter_arete((6, 7), (7, 7))


# Initialisation de Tkinter
TAILLE = 8
WIDTH = 800
MARGE = 10
TAILLE_CASE = (WIDTH-2*MARGE)//TAILLE
w_ajustee = TAILLE_CASE*TAILLE
h_ajustee = w_ajustee

fen_princ = Tk()
fen_princ.geometry("900x900")
fen_princ.bind("<KeyPress-r>", onkeypresse)

# Initialisation du Canvas
monCanvas = Canvas(
    fen_princ,
    width=w_ajustee,
    height=h_ajustee,
    bg='grey',
    border=10
)
monCanvas.pack()

# Initialisation d'un Graphe
monGraphe = Graphe()
configGraphe(monGraphe)
print("👇Voici le graphe 👇\n")
monGraphe.affiche()


# Amélioration de l'affichage de la fenêtre Tk
def represente_laby(canevas: Canvas, G: Graphe):
    """
    Cette fonction configure l'écran pour représenter le Graphe
    sous forme de rectangles avec une couleur spécifique
    """
    for elm in G.sommets():
        ligne, colonne = elm
        ligne *= TAILLE_CASE
        colonne *= TAILLE_CASE
        if len(G.voisins(elm)) == 0:
            canevas.create_rectangle(
                ligne,
                colonne,
                ligne + TAILLE_CASE,
                colonne + TAILLE_CASE,
                fill="blue"
            )
        else:
            canevas.create_rectangle(
                ligne,
                colonne,
                ligne + TAILLE_CASE,
                colonne + TAILLE_CASE,
                fill="white"
            )


def represente_entree_sortie(
    canevas: Canvas,
    G: Graphe,
    entree: tuple,
    sortie: tuple
):
    listSommets = G.sommets()
    if (
        entree not in listSommets and
        sortie not in listSommets
    ):
        return

    ligne, colonne = entree
    ligne *= TAILLE_CASE
    colonne *= TAILLE_CASE
    canevas.create_rectangle(
        ligne,
        colonne,
        ligne + TAILLE_CASE,
        colonne + TAILLE_CASE,
        fill="orange"
    )

    ligne, colonne = sortie
    ligne *= TAILLE_CASE
    colonne *= TAILLE_CASE
    canevas.create_rectangle(
        ligne,
        colonne,
        ligne + TAILLE_CASE,
        colonne + TAILLE_CASE,
        fill="green"
    )


represente_laby(monCanvas, monGraphe)
represente_entree_sortie(monCanvas, monGraphe, (2, 3), (4, 5))

# Lancement de l'intéraction avec l'écran
fen_princ.mainloop()
