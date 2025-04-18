from graphe_dictionnaire_adjacence import *
import parcours_largeur as pl
import parcours_profondeur as pp


#question 1

def affiche(self):
    for key in self.adj:
        print(key, self.voisins(key))
        
g1 = Graphe()
g1.ajouter_arc("A", "B")
g1.ajouter_arc("B", "C")
g1.ajouter_arc("B", "D")
g1.ajouter_arc("B", "E")
g1.ajouter_arc("C", "D")
g1.ajouter_arc("C", "E")
g1.ajouter_arc("D", "B")
g1.ajouter_arc("E", "D")

g1.affiche()

#question 2

def max_voisins(g):
    s_max = None
    v_max = 0
    for key in g.adj:
        if len(g.voisins(key)) > v_max:
            s_max = key
            v_max = len(g.voisins(key))
            
    return s_max

#print('max_voisins(G)=',max_voisins(G))
assert max_voisins(g1) == 'B'

#question 3

def inaccessible(g, x):
    for key in g.adj:
        if x in g.voisins(key):
            return False
    return True
    
assert inaccessible(g1, "D") == False
assert inaccessible(g1, "A") == True
assert inaccessible(g1, "E") == False

#question 4

def voisins_entrants(g, x):
    L = []
    for key in g.adj:
        if x in g.voisins(key):
            L.append(key)
    return L
    
assert voisins_entrants(g1, "B") == ["A", "D"]
assert voisins_entrants(g1, "A") == []
assert voisins_entrants(g1, "C") == ["B"]

#question 5

def distance(g, x, y):
    n = pl.parcours_largeur(g, x)
    if y in pl.parcours_largeur(g, x):
        return n[y]
    else:
        return None
    
assert distance(g1, "A", "D") == 2
assert distance(g1, "D", "A") == None
assert distance(g1, "A", "E") == 2
assert distance(g1, "A", "D") == 2
assert distance(g1, "C", "A") == None