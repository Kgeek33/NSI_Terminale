from une_pile_avec_une_liste_chainée import Pile
from graphe_dictionnaire_adjacence_tbc import Graphe


def existe_parcours_o_cyclique(g: Graphe, sommet):
    s = sommet
    u = sommet
    v = sommet
    p = Pile()
    d = {}
    L = g.sommets()
    for i in L:
        d[i] = "blanc"
    p.empiler(s)
    while not p.est_vide():
        u = p.depiler()
        if d[u] == "noire":
            return True
        
        else:
            d[u] = "noire"
        for voisin in g.voisins(u):
            

if __name__ == "__main__":
    G_1 = Graphe()
    G_1.ajouter_arc("A", "B")
    G_1.ajouter_arc("A", "D")
    G_1.ajouter_arc("B", "C")
    G_1.ajouter_arc("D", "C")
    print(existe_parcours_o_cyclique(G_1, "A"))

    G_2 = Graphe()
    G_2.ajouter_arc("A", "B")
    G_2.ajouter_arc("B", "C")
    G_2.ajouter_arc("C", "D")
    G_2.ajouter_arc("D", "B")

    print(existe_parcours_o_cyclique(G_2, "A"))
