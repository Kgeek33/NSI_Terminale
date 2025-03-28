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


if __name__ == "__main__":
    G_1 = Graphe()
    G_1.ajouter_arrete("A", "B")
    G_1.ajouter_arrete("A", "D")
    G_1.ajouter_arrete("D", "E")
    G_1.ajouter_arrete("E", "B")
    G_1.ajouter_arrete("B", "C")
    G_1.ajouter_arrete("C", "E")
    G_1.ajouter_arrete("C", "F")
    G_1.ajouter_arrete("G", "C")
    G_1.ajouter_arrete("F", "G")
    G_1.ajouter_arrete("G", "H")
    print(parcours_profondeur(G_1, "A"))
