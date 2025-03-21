from une_file_avec_une_liste_chainée import *
from graphe_dictionnaire_adjacence import *


def min_exclu(voisins, coloriage):
    """choix glouton de la couleur d'une sommet
    prend en paramêtre la liste des voisins du sommet et le coloriage en construction, 
    renvoie la plus petite couleur non utilisée par les voisins"""
    
    "à compléter"
    return "à compléter"


def colorier(g):
    """colorie le graphe g avec un algorithme glouton
    renvoie le dctionnaire des couleurs (valeur) associées à chaque sommet (clé),
    ainsi que le nb total de couleurs utilisées"""


    "à compléter"
    return "à compléter","à compléter"



g_regions=Graphe()
g_regions.ajouter_arete('Centre-Val de Loire','Nouvelle-Aquitaine')
g_regions.ajouter_arete('Nouvelle-Aquitaine','Pays de la Loire')
g_regions.ajouter_arete('Nouvelle-Aquitaine','Auvergne-Rhône-Alpes')
g_regions.ajouter_arete('Nouvelle-Aquitaine','Occitanie')
#a compléter...


g_regions.affiche()
print("{} régions, {} arêtes".format(g_regions.ordre(),int(nb_arcs_db_sens(g_regions))))

print()
print("les régions:",g_regions.sommets())

print()
couleurs,nb_couleurs=colorier(g_regions)
print("coloriage :\n",couleurs,"\nen",nb_couleurs,"couleurs")
