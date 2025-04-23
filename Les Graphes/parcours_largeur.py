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


def parcours_largeur_rec(
    g: Graphe,
    source,
    sommets_coches=None,
    file_a_visiter=None
):
    if sommets_coches is None:
        sommets_coches = {source: 0}
    if file_a_visiter is None:
        file_a_visiter = File()
        file_a_visiter.ajouter(source)

    if not file_a_visiter.est_vide():
        sommet = file_a_visiter.retirer()
        for voisin in g.voisins(sommet):
            if voisin not in sommets_coches:
                sommets_coches[voisin] = sommets_coches[sommet] + 1
                file_a_visiter.ajouter(voisin)
        return parcours_largeur_rec(g, source, sommets_coches, file_a_visiter)
    else:
        return sommets_coches


def parcours_arcs(G: Graphe, source):
    sommets_coches = {source: None}
    la_file_courante = File()
    la_file_suivante = File()
    la_file_courante.ajouter(source)
    while not la_file_courante.est_vide():
        sommet = la_file_courante.retirer()
        for voisin in G.voisins(sommet):
            if voisin not in sommets_coches:
                sommets_coches[voisin] = sommet
                la_file_suivante.ajouter(voisin)
        if la_file_courante.est_vide():
            la_file_courante = la_file_suivante
            la_file_suivante = File()
    return sommets_coches


def un_chemin(g, depart, arrivee):
    """ prend en paramètre le graphe, les sommets de depart et d’arrivée,
    et renvoie un chemin sous forme de liste des sommets qui le constituent """
    ch = []
    # construit le dictionnaire des arcs du parcours à partir du depart
    arcs = parcours_arcs(g, depart)
    # reconstitue le chemin à faire
    if arrivee not in arcs.keys():
        return None
    s = arrivee
    while s is not None:
        ch = [s]+ch
        s = arcs[s]
    return ch


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
    print("Parcours_arcs (itératif - 'A') ===>", parcours_arcs(G_1, "A"))
    print("Parcours_arcs (itératif - 'A') ===>", parcours_arcs(G_1, "A"))
    print("Chemin (A - E) ===>", un_chemin(G_1, "A", "E"))
    print("-------------------------------------------------")

    G_2 = Graphe()
    G_2.ajouter_arete("a", "b")
    G_2.ajouter_arete("a", "c")
    G_2.ajouter_arete("b", "d")
    G_2.ajouter_arete("b", "e")
    G_2.ajouter_arete("c", "d")
    G_2.ajouter_arete("d", "e")
    G_2.ajouter_arete("e", "f")
    G_2.ajouter_arete("e", "g")
    G_2.ajouter_arete("f", "g")
    G_2.ajouter_arete("g", "h")
    print("Largeur (itératif - 'g') ===>", parcours_largeur(G_2, "g"))
    print("Largeur (récursif - 'g') ===>", parcours_largeur_rec(G_2, "g"))
    print("Parcours_arcs (itératif - 'g') ===>", parcours_arcs(G_2, "g"))
    print("Chemin (g - d) ===>", un_chemin(G_2, "g", "d"))
    print("-------------------------------------------------")
