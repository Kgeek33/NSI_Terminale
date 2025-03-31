from une_pile_avec_une_liste_chainée import Pile
from graphe_dictionnaire_adjacence_tbc import Graphe


def parcours_profondeur(G: Graphe, sommet) -> list:
    sommets_coches = []
    pile = Pile()
    pile.empiler(sommet)
    while not pile.est_vide():
        s = pile.depiler()
        if s not in sommets_coches:
            sommets_coches.append(s)
        voisins = G.voisins(s)
        for elm in voisins:
            if elm not in sommets_coches:
                pile.empiler(elm)
    return sommets_coches


def parcours_profondeur_rec(G: Graphe, sommet, sommets_coches=None) -> list:
    if sommets_coches is None:
        sommets_coches = []
    if sommet not in sommets_coches:
        sommets_coches.append(sommet)
        voisins = G.voisins(sommet)
        for elm in voisins:
            if elm not in sommets_coches:
                parcours_profondeur_rec(G, elm, sommets_coches)
    return sommets_coches


def existe_chemin(g: Graphe, s, t):
    return t in parcours_profondeur(g, s)


def est_connexe_noriente(g: Graphe):
    cpt = 0
    s1 = g.sommets()[0]
    for s in g.sommets():
        if s in parcours_profondeur(g, s1):
            cpt += 1
    if cpt == len(g.sommets()):
        return True
    return False


if __name__ == "__main__":
    G_1 = Graphe()
    G_1.ajouter_arc("A", "B")
    G_1.ajouter_arc("A", "D")
    G_1.ajouter_arc("D", "E")
    G_1.ajouter_arc("E", "B")
    G_1.ajouter_arc("B", "C")
    G_1.ajouter_arc("C", "E")
    G_1.ajouter_arc("C", "F")
    G_1.ajouter_arc("G", "C")
    G_1.affiche()
    print(parcours_profondeur(G_1, "A"))
    print(parcours_profondeur_rec(G_1, "A"))

    G_2 = Graphe()
    G_2.ajouter_arrete("A", "B")
    G_2.ajouter_arrete("A", "C")
    G_2.ajouter_arrete("B", "D")
    G_2.ajouter_arrete("B", "E")
    G_2.ajouter_arrete("C", "D")
    G_2.ajouter_arrete("D", "E")
    G_2.ajouter_arrete("E", "F")
    G_2.ajouter_arrete("E", "G")
    G_2.ajouter_arrete("F", "G")
    G_2.ajouter_arrete("G", "H")
    G_2.affiche()
    print(parcours_profondeur(G_2, "G"))
    print(parcours_profondeur_rec(G_2, "G"))
    print(parcours_profondeur_rec(G_2, "A"))

    print(existe_chemin(G_1, "A", "G"))
    print(existe_chemin(G_1, "A", "F"))

    G_3 = Graphe()
    G_3.ajouter_arrete("A", "B")
    G_3.ajouter_arrete("D", "C")
    G_3.affiche()
    print(est_connexe_noriente(G_2))
    print(est_connexe_noriente(G_3))
