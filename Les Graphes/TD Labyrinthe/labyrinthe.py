from tkinter import Tk, Canvas
from graphe_dictionnaire_adjacence_tbc import Graphe
# from une_pile_avec_une_liste_chainée import Pile


# Fonctions d'initialisation
def onkeypresse():
    """ Cette fonction s'exécute lorsque la touche `r` est cliquée """
    x = 100
    y = 200
    monCanvas.create_rectangle(x, y, x + 40, y + 40, fill="blue")


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
    for i in range(8):
        for j in range(8):
            if (i, j) not in [(4, 2), (6, 6)]:
                if i > 0 and (i - 1, j) not in [(4, 2), (6, 6)]:
                    THEgraphe.ajouter_arrete((i, j), (i - 1, j))
                if i < 7 and (i + 1, j) not in [(4, 2), (6, 6)]:
                    THEgraphe.ajouter_arrete((i, j), (i + 1, j))
                if j > 0 and (i, j - 1) not in [(4, 2), (6, 6)]:
                    THEgraphe.ajouter_arrete((i, j), (i, j - 1))
                if j < 7 and (i, j + 1) not in [(4, 2), (6, 6)]:
                    THEgraphe.ajouter_arrete((i, j), (i, j + 1))


# Initialisation de Tkinter
fen_princ = Tk()
fen_princ.geometry("900x900")
fen_princ.bind("<KeyPress-r>", onkeypresse)

# Initialisation du Canvas
monCanvas = Canvas(fen_princ, width=800, height=800, bg="green", border=10)
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
        x, y = elm
        x *= 100
        y *= 100
        if len(G.voisins(elm)) == 0:
            canevas.create_rectangle(x, y, x + 40, y + 40, fill="blue")
        else:
            canevas.create_rectangle(x, y, x + 40, y + 40, fill="white")


represente_laby(monCanvas, monGraphe)

# Lancement de l'intéraction avec l'écran
fen_princ.mainloop()
