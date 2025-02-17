# Créé le 10/11/2020 en Python 3.4

import PIL.Image as PIL
img=PIL.open("riad-sattouf-librairies.png")
largeur,hauteur=img.size        # dimensions de l'image en pixels
px=img.load()                   # si 0<=x<largeur et 0<=y<hauteur, la couleur du pixel (x,y) est donnée par px[x,y]
# on peut modifier la couleur d'un pixel (x,y) avec l'affectation px[x,y]=c où c est une couleur
PIL.Image.show(img)


def rotation(px,x,y,t):
    """effectue la rotation de la portion carrée de l'image contenue dans px
    entre les pixels (x,y) et (x+t,y+t).
    t est une puissance de 2
    Ne renvoie rien """
    #rotation de chaque quart
    # cas de base : un pixel tout seul : il tourne sur lui-même et rien ne change...
    ##à completer
    pass


    # un carré non réduit à un point ...
    ##à completer
    
    rotation(px,x,y,t//2)
    rotation(px,x+t//2,y,t//2)
    rotation(px,x,y+t//2,t//2)
    rotation(px,x+t//2,y+t//2,t//2)
    
    

    #deplacement de chaque quart pîxel par pixel vers un autre quart
    ##à completer
    for xx in range(x,t//2):
        for yy in range(y,t//2):
            px_tmp=px[xx,yy+t//2]
            px[xx,yy+t//2]=px[xx,yy]



rotation(px,0,0,largeur)
PIL.Image.show(img)


