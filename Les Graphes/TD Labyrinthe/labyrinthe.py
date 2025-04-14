from tkinter import Tk, Canvas
from random import randint
from graphe_dictionnaire_adjacence_tbc import *




fen_princ = Tk()  # création d'une fenetre
fen_princ.geometry("900x900")  # taille de la fenetre : 900x900
monCanvas = Canvas(fen_princ, width=800, height=800, bg='green', border=10)
# widget canvas
# il permet de dessiner des formes diverses
monCanvas.pack()  # place le widget dans la fenetre
monGraphe = Graphe()

for i in range(8):
    for j in range(8):
        monGraphe.ajouter_sommet((i,j))

# Ajout des arêtes entre les sommets, sauf pour (4, 2) et (6, 6)
for i in range(8):
    for j in range(8):
        if (i, j) not in [(4, 2), (6, 6)]:  # Exclure les sommets (4, 2) et (6, 6)
            if i > 0 and (i - 1, j) not in [(4, 2), (6, 6)]:
                monGraphe.ajouter_arrete((i, j), (i - 1, j))
            if i < 7 and (i + 1, j) not in [(4, 2), (6, 6)]:
                monGraphe.ajouter_arrete((i, j), (i + 1, j))
            if j > 0 and (i, j - 1) not in [(4, 2), (6, 6)]:
                monGraphe.ajouter_arrete((i, j), (i, j - 1))
            if j < 7 and (i, j + 1) not in [(4, 2), (6, 6)]:
                monGraphe.ajouter_arrete((i, j), (i, j + 1))

def represente_laby(canevas:Canvas, G: Graphe):
    for i in G.sommets():
        x, y = i
        x *= 100
        y *= 100
        if len(G.voisins(i)) == 0:
            canevas.create_rectangle(x, y, x + 40, y + 40, fill='blue')
        else:
            canevas.create_rectangle(x, y, x + 40, y + 40, fill='white')

def onkeypresse(event):  # ...
    x = 100
    y = 200
    monCanvas.create_rectangle(x, y, x + 40, y + 40, fill='blue')


# permet d'appeler onkeypressed lorsque l'on appuie sur la touche <r>
fen_princ.bind('<KeyPress-r>', onkeypresse)


# création d'un rectangle de couleur bleue #de dimensions 40x40
# lance le gestionnaire d'événements qui interceptera
# les actions de l'utilisateur
represente_laby(monCanvas, monGraphe)
fen_princ.mainloop()
