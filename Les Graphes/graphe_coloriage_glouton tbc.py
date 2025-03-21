# from une_file_avec_une_liste_chainée import *
from graphe_dictionnaire_adjacence_tbc import Graphe
from random import randint

couleurs = [1, 2, 3, 4]


def valide(g: Graphe, dico_loriage: dict[str, int]) -> bool:
    for s in g.sommets():
        for v in g.voisins(s):
            if s in dico_loriage and v in dico_loriage:
                if dico_loriage[s] == dico_loriage[v]:
                    return False
    return True


def min_exclu(voisins, coloriage):
    """
    choix glouton de la couleur d'une sommet
    prend en paramêtre la liste des voisins du sommet
    et le coloriage en construction, renvoie la plus petite couleur
    non utilisée par les voisins"""

    "à compléter"
    return "à compléter"


def colorier(g: Graphe) -> tuple[dict, int]:
    """
    colorie le graphe g avec un algorithme glouton
    renvoie le dctionnaire des couleurs (valeur)
    associées à chaque sommet (clé), ainsi que
    le nb total de couleurs utilisées
    """
    d = {}
    nb_couleurs = len(couleurs)
    for key in g.sommets():
        for v in g.voisins(key):
            if d[key] == d[v]:
                while d[key] == d[v]:
                    d[key] = randint(couleurs[0], couleurs[len(couleurs)-1])
        else:
            d[key] = randint(couleurs[0], couleurs[len(couleurs)-1])
            
    return (d, nb_couleurs)


g_regions = Graphe()
g_regions.ajouter_arrete("Centre-Val de Loire", "Nouvelle-Aquitaine")
g_regions.ajouter_arrete("Nouvelle-Aquitaine", "Pays de la Loire")
g_regions.ajouter_arrete("Nouvelle-Aquitaine", "Auvergne-Rhône-Alpes")
g_regions.ajouter_arrete("Centre-Val de Loire", "Pays de la Loire")
g_regions.ajouter_arrete("Centre-Val de Loire", "Normandie")
g_regions.ajouter_arrete("Centre-Val de Loire", "Île-de-France")
g_regions.ajouter_arrete("Centre-Val de Loire", "Auvergne-Rhône-Alpes")
g_regions.ajouter_arrete("Centre-Val de Loire", "Bougone-Franche-Comte")
g_regions.ajouter_arrete("Pays de la Loire", "Normandie")
g_regions.ajouter_arrete("Pays de la Loire", "Bretagne")
g_regions.ajouter_arrete("Bretagne", "Normandie")
g_regions.ajouter_arrete("Normandie", "Île-de-France")
g_regions.ajouter_arrete("Normandie", "Hauts de-France")
g_regions.ajouter_arrete("Hauts de-France", "Grand Est")
g_regions.ajouter_arrete("Hauts de-France", "Île-de-France")
g_regions.ajouter_arrete("Île-de-France", "Grand Est")
g_regions.ajouter_arrete("Île-de-France", "Bougone-Franche-Comte")
g_regions.ajouter_arrete("Bougone-Franche-Comte", "Grand Est")
g_regions.ajouter_arrete("Bougone-Franche-Comte", "Auvergne-Rhône-Alpes")
g_regions.ajouter_arrete("Auvergne-Rhône-Alpes", "Provence-Ales-Côte-d'Azure")
g_regions.ajouter_arrete("Provence-Ales-Côte-d'Azure", "Occitanie")
g_regions.ajouter_arrete("Nouvelle-Aquitaine", "Occitanie")
g_regions.ajouter_arrete("Occitanie", "Auvergne-Rhône-Alpes")

g_regions.affiche()
# print("{} régions, {} arêtes".format(
#     g_regions.ordre(), int(g_regions.nb_arcs_db_sens())))

print()
print("les régions:", g_regions.sommets())


dicotest = {
    "Centre-Val de Loire": 1,
    "Nouvelle-Aquitaine": 2,
    "Pays de la Loire": 3,
    "Auvergne-Rhône-Alpes": 4,
    "Normandie": 1,
    "Île-de-France": 2,
    "Bougone-Franche-Comte": 3,
    "Bretagne": 4,
    "Hauts de-France": 1,
    "Grand Est": 2,
    "Provence-Ales-Côte-d'Azure": 3,
    "Occitanie": 4,
}

dicotest2 = {
    "Centre-Val de Loire": 4,
    "Nouvelle-Aquitaine": 1,
    "Pays de la Loire": 3,
    "Auvergne-Rhône-Alpes": 3,
    "Normandie": 2,
    "Île-de-France": 3,
    "Bougone-Franche-Comte": 2,
    "Bretagne": 1,
    "Hauts de-France": 4,
    "Grand Est": 1,
    "Provence-Ales-Côte-d'Azure": 4,
    "Occitanie": 2,
}

print(valide(g_regions, dicotest))
print(valide(g_regions, dicotest2))
# couleurs, nb_couleurs = colorier(g_regions)
# print("coloriage :\n", couleurs, "\nen", nb_couleurs, "couleurs")
