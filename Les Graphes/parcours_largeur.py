from une_file_avec_une_liste_chainée import File
from graphe_dictionnaire_adjacence_tbc import Graphe


def parcours_largeur(G: Graphe, source):
    sommets_coches = {source: 0}
    la_file_courante = File()
    la_file_suivante = File()
    la_file_courante.ajouter(source)
    d = 0
    while not la_file_courante.est_vide():
        sommet = la_file_courante.retirer()
        for voisin in G.voisins(sommet):
            if voisin not in sommets_coches:
                sommets_coches[voisin] = d + 1
                la_file_suivante.ajouter(voisin)
        if la_file_courante.est_vide():
            la_file_courante = la_file_suivante
            la_file_suivante = File()
            d += 1
    return sommets_coches


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
    print("Largeur (itératif - 'A') ===>", parcours_largeur(G_1, "A"))
    print("-------------------------------------------------")

    G_2 = Graphe()
    G_2.ajouter_arrete("a", "b")
    G_2.ajouter_arrete("a", "c")
    G_2.ajouter_arrete("b", "d")
    G_2.ajouter_arrete("b", "e")
    G_2.ajouter_arrete("c", "d")
    G_2.ajouter_arrete("d", "e")
    G_2.ajouter_arrete("e", "f")
    G_2.ajouter_arrete("e", "g")
    G_2.ajouter_arrete("f", "g")
    G_2.ajouter_arrete("g", "h")
    print("Largeur (itératif - 'g') ===>", parcours_largeur(G_2, "g"))
    print("-------------------------------------------------")
