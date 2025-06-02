from graphe_dictionnaire_adjacence import *
import parcours_largeur as pl
import parcours_profondeur as pp


# question 1
print("Question 1 :")
G = Graphe()
G.ajouter_arc("A", "B")
G.ajouter_arc("B", "C")
G.ajouter_arc("B", "D")
G.ajouter_arc("B", "E")
G.ajouter_arc("C", "D")
G.ajouter_arc("C", "E")
G.ajouter_arc("D", "B")
G.ajouter_arc("E", "D")

G.affiche()

# question 2
print("\nQuestion 2 :")


def max_voisins(g: Graphe):
    lettre = g.sommets()[0]
    nombreVoisins = len(g.voisins(lettre))
    for s in g.sommets():
        nbVoisins = len(g.voisins(s))
        if nbVoisins >= nombreVoisins:
            lettre = s
            nombreVoisins = nbVoisins
    return lettre


print('max_voisins(G)=', max_voisins(G))

assert max_voisins(G) == 'B'

# question 3
print("\nQuestion 3 :")


def inaccessible(g: Graphe, x):
    for s in g.sommets():
        for t in g.voisins(s):
            if t == x:
                return False
    return True


print('inaccessible(G, "D")=',inaccessible(G, "D"))
print('inaccessible(G, "A")=',inaccessible(G, "A"))
assert inaccessible(G, "D") == False
assert inaccessible(G, "A") == True

# question 4
print("\nQuestion 4 :")


def voisins_entrants(g: Graphe, x):
    UNEliste = []
    for s in g.sommets():
        LESvoisins = g.voisins(s)
        if x in LESvoisins:
            UNEliste.append(s)
    return UNEliste


print('voisins_entrants(G, "B")=',voisins_entrants(G, "B"))
assert voisins_entrants(G, "B") == (["A", "D"] or ["D", "A"])

# question 5
print("\nQuestion 5 :")
# def distance(g: Graphe, x, y):
#     for t in g.voisins(x):
#         LESvoisins = g.voisins(t)
#         for num in range(len(LESvoisins)):
#             if LESvoisins[num] == y:
#                 return num + 1
#     return None


def distance(g: Graphe, x, y):
    largeur = pl.parcours_largeur(g, x)
    if y not in largeur:
        return None
    return largeur[y]

print('distance(G, "A", "D")=',distance(G, "A", "D"))
print('distance(G, "D", "A")=',distance(G, "D", "A"))
print('distance(G, "A", "E")=',distance(G, "A", "E"))
assert distance(G, "A", "D") == 2
assert distance(G, "D", "A") == None
assert distance(G, "A", "E") == 2
