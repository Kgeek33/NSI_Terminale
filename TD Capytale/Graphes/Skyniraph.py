from graphe_dictionnaire_adjacence import *
import parcours_largeur as pl
import parcours_profondeur as pp


#question 1

G = Graphe()
G.ajouter_arc("A","B")
G.ajouter_arc("B","C")
G.ajouter_arc("B","D")
G.ajouter_arc("D","B")
G.ajouter_arc("C","D")
G.ajouter_arc("C","E")
G.ajouter_arc("E","D")
G.ajouter_arc("B","E")
G.affiche()

#question 2

def max_voisins(g: Graphe) -> str:
    s_max =None
    max_n = 0
    for s in g.sommets():
        if len(g.voisins(s)) > max_n:
            s_max = s
            max_n = len(g.voisins(s))
    return s_max
        

print('max_voisins(G)=',max_voisins(G))

assert max_voisins(G)=="B" 

#question 3

def inaccessible(g,x):
    for s in g.sommets():
        if x in g.voisins(s):
            return True
    return False
    
assert inaccessible(G,"D") == True
assert inaccessible(G,"A") == False
#question 4

def voisins_entrants(g,x):
    v_entrants = []
    for s in g.sommets():
        if x in g.voisins(s):
            v_entrants.append(s)
    return v_entrants
    
print(voisins_entrants(G,"B"))

#question 5
# à compléter