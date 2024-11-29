from random import randint
import snake_pygame as spg

BLACK=(0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE= (0,0,255)
WHITE=(255,255,255)
YELLOW=(255,255,0)
PURPLE=(89,27,219)



class Point :
    #attribut de classe : définit la taille d'un point (taille du côté) en pixels
    taille_pxl=20
    
    def __init__(self,x_m,y_m,x,y,c):
        """x_m et y_m (entiers) definissent le max en x et en y,
        x et y (entiers) les coordonnées du point et
        c (tuple RGB) sa couleur """
        self.x_max=x_m
        self.y_max=y_m
        self.abs=max(min(x,self.x_max),0)
        self.ord=max(min(y,self.y_max),0)
        self.couleur=c
    
    def __str__(self):
        """renvoie une chaine sous la forme '(x,y)'"""
        pass
        return "Point.__str__ a completer"

    
    def __eq__(self,p):
        """deux points sont egaux ssi ils ont les mêmes coordonnées (couleur indifférente),
        renvoie un booléen"""
        pass
    
    def placer(self):
        """place le point dans le jardin (affichage dans la fenetre graphique)"""
        pass
        
    def effacer(self):
        pass
    
class Pomme :
    bonus_pomme_rouge=5
    
    def __init__(self,pt,d):
        """pt est une instance de la classe Point et d un entier désignant la durée de vie de la pomme"""
        pass    

    def pourrie(self,j=1):
        "décompose la pomme et renvoie True si la pomme a depassé sa duree de vie, False sinon"
        pass
    
    def jeter(self):
        """fait disparaitre la pomme du jardin"""
    #
    # ... et d'autres methodes si besoin...
    # 
    
    def __str__(self):
        """renvoie une chaine donnant l'état des attributs d'instances"""
        return "Pomme.__str__ a completer"


class Snake :
    def __init__(self,x_m,y_m,c)  :
        """x_m et y_m (entiers) definissent le max en x et en y de la zone dans laquelle pourra évoluer le serpent,
        c sa couleur (tuple RGB)"""

        # la vitesse est la dernière vitesse demandée par le joueur
        # si le joueur relache les fleches de direction, le serpent continue sur son élan
        self.vitesse=(0,0)
        # le corps est une liste de 1 seul point quelque part dans le jardin
        self.corps = "à completer"
        # et les autres attributs :
        pass
    
    def __len__(self):
        """renvoie la longueur du serpent"""
        return len(self.corps)
    
    def __str__(self):
        pass
        return "Snake.__str__ a completer"
    
    def contient(self,x,y):
        """renvoie True si les coordonnées x,y sont celles d'un point du corps du serpent"""
        pass
    
    def get_tete(self):
        """renvoie le point de tête"""
        pass
    def get_queue(self):
        """renvoie le point de queue"""
        pass
    def get_corps_sans_tete(self):
        """renvoie la liste des points sans la tête""" 
        pass

    def avale(self,pomme):
        """pomme est une instance de Pomme.
        fait grandir le corps par le haut (la tête) dans le sens de deplacement courant"""
        assert self.get_tete()==pomme.point
        pass

    def peut_manger(self,pomme):
        """pomme est une instance de Pomme
        renvoie True si la tête est sur la pomme"""
        pass

    def se_deplace(self,vitesse):
        """ deplace le serpent dans le sens de la vitesse (couple (Vx,Vy) passée en parametre)
        
        maintient un attribut *vivant* comme suit
        le serpent ne reste vivant que
        * si le deplacement le maintient dans les limites du jardin
        * si le deplacement n'est pas un retournenemnt
        """
        
        print(str(self))
        pass
    
    def se_mord_la_queue(self):
        """ renvoie True et tue le serpent si la tete coincide avec une autre partie du corps"""
        pass
        
        
# les tests du module   
if __name__ == '__main__' :
    DIM_X, DIM_Y = 40, 30 # nombre de cases (point) en x et en y dans la fenetre
    H_SCORE_EN_PXL = 40 # hauteur du panneau de score en pixels
    spg.fenetre_init(DIM_X, DIM_Y,H_SCORE_EN_PXL,Point.taille_pxl)
    
    #tests de la classe Point
    point_A=Point(20,10,2,3,BLUE)
    print(str(point_A))
    point_A.placer()
    point_B=Point(20,10,25,-3,GREEN)
    print(str(point_B))
    point_B.placer()
    L_COLORS=[BLACK,YELLOW,RED,PURPLE]
    for k in range(4):
        point_B=Point(20,10,25,-3,L_COLORS[randint(1,len(L_COLORS))-1])
        print(str(point_B))
        point_B.placer()
        spg.attente(1000)
        point_B.effacer()

    #tests de la classe Pomme


    #tests de la classe Snake
    mon_snake=Snake(DIM_X, DIM_Y,(19, 244, 234))
    mon_snake.se_deplace((0,1))
    # a completer : test en ligne droite, en zig-zag
    # a completer : test de rencontres avec des pommmes et croissance du serpent

