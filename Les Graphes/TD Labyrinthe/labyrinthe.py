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
    THEgraphe.ajouter_arete((5, 0), (6, 0))
    THEgraphe.ajouter_arete((6, 0), (6, 1))
    THEgraphe.ajouter_arete((6, 1), (7, 1))
    THEgraphe.ajouter_arete((7, 1), (7, 2))
    THEgraphe.ajouter_arete((4, 2), (4, 3))
    THEgraphe.ajouter_arete((4, 3), (4, 4))
    THEgraphe.ajouter_arete((4, 3), (5, 3))
    THEgraphe.ajouter_arete((5, 3), (6, 3))
    THEgraphe.ajouter_arete((4, 4), (3, 4))
    THEgraphe.ajouter_arete((3, 4), (3, 5))
    THEgraphe.ajouter_arete((3, 5), (3, 6))
    THEgraphe.ajouter_arete((3, 6), (2, 6))
    THEgraphe.ajouter_arete((2, 6), (2, 7))
    THEgraphe.ajouter_arete((2, 6), (1, 6))
    THEgraphe.ajouter_arete((1, 6), (0, 6))
    THEgraphe.ajouter_arete((0, 6), (0, 7))
    THEgraphe.ajouter_arete((3, 6), (4, 6))
    THEgraphe.ajouter_arete((4, 6), (4, 7))
    THEgraphe.ajouter_arete((4, 7), (5, 7))
    THEgraphe.ajouter_arete((5, 7), (6, 7))
    THEgraphe.ajouter_arete((6, 7), (7, 7))
    THEgraphe.ajouter_arete((6, 7), (6, 6))
    THEgraphe.ajouter_arete((6, 6), (6, 5))
    THEgraphe.ajouter_arete((6, 5), (5, 5))
    THEgraphe.ajouter_arete((6, 5), (7, 5))
    THEgraphe.ajouter_arete((7, 5), (7, 4))


def generation_graphe(M: list[list[int]]) -> Graphe:
    """
    Cette fonction crée un graphe depuis une matrice et
    configure les sommets et les arrêtes du graphe
    """
    UNgraphe = Graphe()
    for i in range(len(M)):
        for j in range(len(M[i])):
            UNgraphe.ajouter_sommet((i, j))
            if M[i][j] == 1:
                if i > 0 and M[i - 1][j] == 1:
                    UNgraphe.ajouter_arete((i, j), (i - 1, j))
                if j > 0 and M[i][j - 1] == 1:
                    UNgraphe.ajouter_arete((i, j), (i, j - 1))
                if i < len(M) - 1 and M[i + 1][j] == 1:
                    UNgraphe.ajouter_arete((i, j), (i + 1, j))
                if j < len(M[i]) - 1 and M[i][j + 1] == 1:
                    UNgraphe.ajouter_arete((i, j), (i, j + 1))
    return UNgraphe


# Initialisation de Tkinter
CHOIX = "matrice"  # Choix entre "graphe" et "matrice"
TAILLE = 8
WIDTH = 600
MARGE = 10
TAILLE_CASE = (WIDTH - 2 * MARGE) // TAILLE
w_ajustee = TAILLE_CASE * TAILLE
h_ajustee = w_ajustee

fen_princ = Tk()
fen_princ.geometry("700x700")

# Initialisation du Canvas
monCanvas = Canvas(
    fen_princ,
    width=w_ajustee,
    height=h_ajustee,
    bg="grey",
    border=10
)
monCanvas.pack()

# Initialisation d'un Graphe
monGraphe = Graphe()
configGraphe(monGraphe)

# Initialisation d'une matrice sous forme de graphe
maMatrice = [
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1],
]
matriceGraphe = generation_graphe(maMatrice)


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
    """
    Cette fonction configure l'écran pour représenter
    l'entrée et la sortie du labyrinthe
    """
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
    """
    Cette fonction représente le chemin trouvé entre
    l'entrée et la sortie du labyrinthe
    lorsque l'on appuie sur 'r'
    """
    chemin = un_chemin(G, entree, sortie)
    if chemin is None:
        print("Aucun chemin trouvé")
        return
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


if CHOIX == "graphe":
    print("👇Voici le graphe 👇\n")
    monGraphe.affiche()

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
elif CHOIX == "matrice":
    print("👇Voici la matrice sous forme de graphe 👇\n")
    matriceGraphe.affiche()

    represente_laby(monCanvas, matriceGraphe)
    represente_entree_sortie(monCanvas, matriceGraphe, (0, 0), (7, 7))
    fen_princ.bind(
        "<KeyPress-r>",
        lambda _: represente_chemin(
            monCanvas,
            matriceGraphe,
            (0, 0),
            (7, 7),
        )
    )

# Lancement de l'intéraction avec l'écran
fen_princ.mainloop()
