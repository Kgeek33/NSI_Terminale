from tkinter import *


fen_princ = Tk() #création d'une fenetre
fen_princ.geometry("900x900") #taille de la fenetre : 900x900
monCanvas = Canvas(fen_princ, width=800, height=800, bg='green',border = 10)  
#widget canvas
#il permet de dessiner des formes diverses
monCanvas.pack() #place le widget dans la fenetre

def onkeypresse(event): #...
    x=100
    y=200
    monCanvas.create_rectangle(x, y, x + 40, y + 40, fill='blue')


fen_princ.bind('<KeyPress-r>', onkeypresse) #permet d'appeler onkeypressed lorsque l'on appuie sur la touche <r>

    
#création d'un rectangle de couleur bleue #de dimensions 40x40
fen_princ.mainloop() #lance le gestionnaire d'événements qui interceptera les actions de l'utilisateur
