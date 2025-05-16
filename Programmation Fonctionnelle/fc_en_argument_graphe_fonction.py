# Créé le 24/08/2020 en Python 3.4

import matplotlib.pyplot as plt

def tracer_graphe(f,a = -2,b = 4,n = 500):
    x = a
    for k in range(n+1):
        plt.plot(x,f(x),'r',marker ='.',ms = 2)
        x = x + (b-a)/n

    ax = plt.gca()                                           # définir les axes comme objet modifiable
    ax.spines['right'].set_color('none')                     #effacer le bord droit
    ax.spines['top'].set_color('none')                       #effacer le bord haut
    ax.spines['bottom'].set_position(('data',0))             # place l'axe des abscisses
    ax.spines['left'].set_position(('data',0))               # place l'axe des ordonnées
    #plt.xticks([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4])
    #plt.yticks([0,4,8,12,16])
    plt.grid()
    #plt.xlabel('axe des abscisses')                         # titre de l'axe des abscisses
    #ax.xaxis.set_label_coords(0.9, 0.35)                    # positionne le titre de l'axe des abscisses à 80% de la taille
    plt.show()

def fc_carre(x):
    return x*x


import math

if __name__ == '__main__' :
    tracer_graphe(fc_carre,-3,3)
    tracer_graphe(lambda x: math.exp(x))
    tracer_graphe(lambda x: x**2)
    tracer_graphe(lambda x: -0.5*x**2+1,-3,3)
    tracer_graphe(lambda x: 1/(x+4)+3,-3,3)

