from une_file_avec_une_liste_chainée import *
from graphe_dictionnaire_adjacence import *
from random import shuffle

def min_exclu(voisins, coloriage):
    """choix glouton de la couleur d'une sommet
    prend en paramêtre la liste des voisins du sommet et le coloriage en construction, 
    renvoie la plus petite couleur non utilisée par les voisins"""
    n = len(voisins)
    # état des lieux des couleurs utilisées dans le voisinage consigné dans dispo (liste)
    # la palette de couleurs à utiliser est ajustée entre 0 et n,
    # soit une couleur de plus que le nb de voisins
    dispo = [True] * (n + 1)
    # dispo[couleur] est vrai si couleur n'est utilisée par aucun voisin
    for v in voisins:
        # si le voisin est colorié avec une couleur 
        if v in coloriage and coloriage[v] <= n:
            dispo[coloriage[v]] = False
    # on renvoie la plus petite des couleurs disponibles
    # elle existe nécessairement puisque il y a une couleur de plus que le nb de voisins
    for c in range(n + 1):
        if dispo[c]:
            return c
    assert False # on n'arrivera jamais ici, sauf bug

def colorier(g):
    """colorie le graphe g avec un algorithme glouton
    renvoie le dctionnaire des couleurs (valeur) associées à chaque sommet (clé),
    ainsi que le nb total de couleurs utilisées"""
    coloriage = {}
    nb_couleurs = 0
    sommets_ordonnés=g.sommets()
    # le colriage et le nb de couleurs obtenues dépend de l'ordre de traitement des régions
    shuffle(sommets_ordonnés)
    print("ordre de traitement des sommets : ")
    print(sommets_ordonnés)
    for s in sommets_ordonnés:
        #choix de la couleur du sommet s
        c = min_exclu(g.voisins(s), coloriage)
        coloriage[s] = c
        nb_couleurs = max(nb_couleurs, c + 1)
    return coloriage, nb_couleurs


def valide(g,dico_loriage):
    """prend en parametre le graphe et le dico de coloriage et
    renvoie un booleen qui précise si le coloriage est valide ou non"""
    for s in dico_loriage:
        for v in g.voisins(s):
            if not v in dico_loriage :
                print("coloriage incomplet")
                return False
            if dico_loriage[s]==dico_loriage[v] :
                print("les voisins {} et {} sont de la même couleur".format(s,v))
                return False
    # tout est vérifié
    return True
    


g_regions=Graphe()
g_regions.ajouter_arete('Auvergne-Rhône-Alpes','Occitanie')
g_regions.ajouter_arete('Bourgogne-Franche-Comté','Centre-Val de Loire')
g_regions.ajouter_arete('Ile-de-France','Centre-Val de Loire')
g_regions.ajouter_arete('Ile-de-France','Normandie')
g_regions.ajouter_arete('Ile-de-France','Hauts-de-France')
g_regions.ajouter_arete('Ile-de-France','Grand-Est')
g_regions.ajouter_arete('Hauts-de-France','Grand-Est')
g_regions.ajouter_arete('Hauts-de-France','Normandie')
g_regions.ajouter_arete('Bretagne','Pays de la Loire')
g_regions.ajouter_arete('Centre-Val de Loire','Nouvelle-Aquitaine')
g_regions.ajouter_arete('Nouvelle-Aquitaine','Pays de la Loire')
g_regions.ajouter_arete("Provence-Alpes-Côte d'Azur",'Occitanie')
g_regions.ajouter_arete('Auvergne-Rhône-Alpes',"Provence-Alpes-Côte d'Azur")
g_regions.ajouter_arete('Auvergne-Rhône-Alpes','Centre-Val de Loire')
g_regions.ajouter_arete('Bretagne','Normandie')
g_regions.ajouter_arete('Nouvelle-Aquitaine','Auvergne-Rhône-Alpes')
g_regions.ajouter_arete('Nouvelle-Aquitaine','Occitanie')
g_regions.ajouter_arete('Normandie','Pays de la Loire')
g_regions.ajouter_arete('Pays de la Loire','Centre-Val de Loire')
g_regions.ajouter_arete('Centre-Val de Loire','Normandie')
g_regions.ajouter_arete('Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté')
g_regions.ajouter_arete('Ile-de-France','Bourgogne-Franche-Comté')
g_regions.ajouter_arete('Grand-Est','Bourgogne-Franche-Comté')

g_regions.affiche()
print(g_regions.ordre(),nb_arcs_db_sens(g_regions))

print()
print("les régions:",g_regions.sommets())

print()
couleurs,nb_couleurs=colorier(g_regions)
print("coloriage :\n",couleurs,"\nen",nb_couleurs,"couleurs")

# pour vérifier la coloration obtenue
assert valide(g_regions,couleurs)
