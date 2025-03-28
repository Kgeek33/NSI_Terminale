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
            pile.empiler(elm)
    return sommets_coches


if __name__ == "__main__":
    G_1 = Graphe()
    G_1.ajouter_arrete("a", "b")
    G_1.ajouter_arrete("a", "d")
    G_1.ajouter_arrete("d", "e")
    G_1.ajouter_arrete("e", "b")
    G_1.ajouter_arrete("b", "c")
    G_1.ajouter_arrete("c", "e")
    G_1.ajouter_arrete("c", "f")
    G_1.ajouter_arrete("g", "c")
    G_1.ajouter_arrete("f", "g")
    G_1.ajouter_arrete("g", "h")
    print(parcours_profondeur(G_1, "a"))
