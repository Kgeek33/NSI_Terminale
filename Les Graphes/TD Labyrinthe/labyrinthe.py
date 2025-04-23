from tkinter import Tk, Canvas
from graphe_dictionnaire_adjacence_tbc import Graphe
from parcours_largeur import un_chemin


# Fonctions d'initialisation
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
    THEgraphe.ajouter_arete((0, 2), (1, 2))
    THEgraphe.ajouter_arete((1, 2), (2, 2))
    THEgraphe.ajouter_arete((2, 2), (3, 2))
    THEgraphe.ajouter_arete((3, 2), (3, 3))
    THEgraphe.ajouter_arete((3, 3), (3, 4))
    THEgraphe.ajouter_arete((3, 4), (4, 4))
    THEgraphe.ajouter_arete((4, 4), (5, 4))
    THEgraphe.ajouter_arete((5, 4), (6, 4))
    THEgraphe.ajouter_arete((6, 4), (7, 4))
    THEgraphe.ajouter_arete((7, 4), (7, 5))
    THEgraphe.ajouter_arete((7, 5), (7, 6))
    THEgraphe.ajouter_arete((7, 6), (7, 7))
    THEgraphe.ajouter_arete((0, 0), (1, 0))
    THEgraphe.ajouter_arete((0, 0), (2, 0))
    THEgraphe.ajouter_arete((0, 0), (3, 0))
    THEgraphe.ajouter_arete((0, 0), (4, 0))
    THEgraphe.ajouter_arete((0, 0), (5, 0))
    THEgraphe.ajouter_arete((0, 0), (6, 0))
    THEgraphe.ajouter_arete((0, 0), (7, 0))
    THEgraphe.ajouter_arete((0, 0), (7, 1))
    THEgraphe.ajouter_arete((0, 0), (7, 2))
    THEgraphe.ajouter_arete((0, 0), (7, 3))


# Initialisation de Tkinter
TAILLE = 8
WIDTH = 600
MARGE = 10
TAILLE_CASE = (WIDTH-2*MARGE)//TAILLE
w_ajustee = TAILLE_CASE*TAILLE
h_ajustee = w_ajustee

fen_princ = Tk()
fen_princ.geometry("700x700")

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


def represente_chemin(
    canevas: Canvas,
    G: Graphe,
    entree: tuple,
    sortie: tuple
):
    chemin = un_chemin(G, entree, sortie)
    print(chemin)

    for i in range(len(chemin) - 1):
        x1, y1 = chemin[i]
        x2, y2 = chemin[i + 1]
        x1 *= TAILLE_CASE
        y1 *= TAILLE_CASE
        x2 *= TAILLE_CASE
        y2 *= TAILLE_CASE
        canevas.create_line(
            x1 + TAILLE_CASE // 2,
            y1 + TAILLE_CASE // 2,
            x2 + TAILLE_CASE // 2,
            y2 + TAILLE_CASE // 2,
            fill="red",
            width=5
        )


represente_laby(monCanvas, monGraphe)
represente_entree_sortie(monCanvas, monGraphe, (0, 0), (7, 7))
fen_princ.bind(
    "<KeyPress-r>",
    lambda _: represente_chemin(
        monCanvas,
        monGraphe,
        (0, 0),
        (7, 7),
    )
)

# Lancement de l'intéraction avec l'écran
fen_princ.mainloop()
