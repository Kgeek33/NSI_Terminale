from tkinter import Tk, Canvas
from graphe_dictionnaire_adjacence_tbc import Graphe
from une_pile_avec_une_liste_chainée import Pile


fen_princ = Tk()  # création d'une fenetre
fen_princ.geometry("900x900")  # taille de la fenetre : 900x900
monCanvas = Canvas(fen_princ, width=800, height=800, bg='green', border=10)
monGraphe = Graphe()
for i in range(8):
    for j in range(8):
        monGraphe.ajouter_sommet((i, j))
# widget canvas
# il permet de dessiner des formes diverses
monCanvas.pack()  # place le widget dans la fenetre

def represente_laby(canevas: Canvas, G: Graphe):
    for elm in G.sommets():
        x, y = elm
        x *= 100
        y *= 100
        if len(G.voisins(elm)) == 0:
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
# monGraphe.affiche()
represente_laby(monCanvas, monGraphe)
fen_princ.mainloop()
