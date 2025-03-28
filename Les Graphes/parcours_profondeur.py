from une_pile_avec_une_liste_chainée import Pile
from graphe_matrice_adjacence import Graphe, num


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
    G_1 = Graphe(7)
    G_1.ajouter_arete(num("a"), num("b"))
    G_1.ajouter_arete(num("a"), num("d"))
    G_1.ajouter_arete(num("d"), num("e"))
    G_1.ajouter_arete(num("e"), num("b"))
    G_1.ajouter_arete(num("b"), num("c"))
    G_1.ajouter_arete(num("c"), num("e"))
    G_1.ajouter_arete(num("c"), num("f"))
    G_1.ajouter_arete(num("g"), num("c"))
    G_1.ajouter_arete(num("f"), num("g"))
    G_1.ajouter_arete(num("g"), num("h"))
    print(parcours_profondeur(G_1, num("A")))
