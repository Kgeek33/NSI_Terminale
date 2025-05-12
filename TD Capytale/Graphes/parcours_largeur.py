from une_file_avec_une_liste_chainee import *
from graphe_dictionnaire_adjacence import *

def parcours_largeur(g,source):
    
    """prend un graphe g  et source, l'un de ses sommets, en parametre;
    renvoie le dictionnaire des sommets de g parcourus dans un parcours en profondeur"""

    print("parcours_largeur : ",end="")
    # file des sommets à visiter à la même distance d de la source
    cercle_courant=File()
    # file des sommets à visiter à la distance d+1 de la source
    cercle_suivant=File()
    # clé:valeur = sommet:distance à la source
    sommets_coches={source:0}
    
    d=0 # distance à la source des sommets visités
    cercle_courant.ajouter(source)
    while not cercle_courant.est_vide():
        s= cercle_courant.retirer()
        
        for v in g.voisins(s):
            if v not in sommets_coches:
                sommets_coches[v]=d+1
                cercle_suivant.ajouter(v)
##              print(sommets_coches)
        if cercle_courant.est_vide() :
            # on s'éloigne
            cercle_courant,cercle_suivant=cercle_suivant,cercle_courant
            cercle_suivant.vider()
            d+=1
    print()
    return sommets_coches


# version récursive
def parcours_largeur_rec(g,source,sommets_coches=None,file_a_visiter=None):
    """
    1.  on retire de la_file une variable s (on l’affiche)
    2.  pour chaque voisins non déjà visité de s
    3.  on le note comme visité
    4.  on l’ajoute à la_file
    5.  on recommence du 1
    Le processus s’arrête quand la_file est vide"""
    print("parcours_largeur recursif : ",end="")
    # file des sommets à visiter 
    if file_a_visiter==None : # premier appel de la focntion
        file_a_visiter=File()
        file_a_visiter.ajouter(source)
        sommets_coches={source:0}
        
    if file_a_visiter.est_vide(): # parcours fini
        return sommets_coches
    s= file_a_visiter.retirer()
    for v in g.voisins(s):
        if v not in sommets_coches:
            sommets_coches[v]=sommets_coches[s]+1
            file_a_visiter.ajouter(v)
    parcours_largeur_rec(g,source,sommets_coches,file_a_visiter)
    return sommets_coches


def existe_chemin(g, s, t):
    """existe-t-il un chemin de u à v ?"""
    return t in parcours_largeur(g, s)


def est_connexe(g):
    """uniquement pour un graphe non orienté.
    on utilise la propriété suivante : le graphe est connexe s'il existe un chemin dans le graphe qui contient tous les sommets
    cad le parcours du graphe contient tous les sommets
    """
    sommets=g.sommets()
    # dans un parcours chaque sommet ne peut apparaitre qu'une seule fois
    return len(sommets)==len(parcours_largeur(g,sommets[0]))

#distance entre deux sommets
def distance(g, u, v):
    """renvoie la distance de u à v (et None si pas de chemin)"""
    dist = parcours_largeur(g, u)
    # le parcours en largeur fournit directement la distance à la source u
    if v in dist : return dist[v]
    else : None



# chemin entre deux sommets
def parcours_arcs(g,depart):
    """renvoie le dictionnaire des arcs parcourus où la clé est l’extrémité de l’arc et la valeur est l’origine de l’arc"""
    # arcs_coches est le dictionnaire à construire à partir du sommet depart en parcourant le graphe en largeur 
#    print("parcours_largeur_arcs : ",end="")
    # file des sommets à visiter à la même distance d de la source
    cercle_courant=File()
    # file des sommets à visiter à la distance d+1 de la source
    cercle_suivant=File()
    # dictionnaire {clé:valeur = extremité de l'arc:origine de l'arc}
    arcs_coches={depart:None}
    
    cercle_courant.ajouter(depart)
    while not cercle_courant.est_vide():
        s= cercle_courant.retirer()
        for v in g.voisins(s):
            if v not in arcs_coches:
                arcs_coches[v]=s
                cercle_suivant.ajouter(v)
#                print(arcs_coches)
        if cercle_courant.est_vide() :
            # print("on s'éloigne...")
            cercle_courant,cercle_suivant=cercle_suivant,cercle_courant
            cercle_suivant.vider()

#    print()
    return arcs_coches

def un_chemin(g,depart,arrivee):
    """ prend en paramètre le graphe, les sommets de depart et d’arrivée,
    et renvoie un chemin sous forme de liste des sommets qui le constituent """
    ch=[]
    #construit le dictionnaire des arcs du parcours à partir du depart
    arcs=parcours_arcs(g,depart)
    #print("en largeur",arcs)
    # reconstitue le chemin à faire 
    if not arrivee in arcs.keys(): return None
    s=arrivee
    while s != None:
        ch=[s]+ch
        s=arcs[s]
    return ch


if __name__ == '__main__' :
    
    #creation de G_1
    G_1=Graphe()
    G_1.ajouter_arc('A','B')
    G_1.ajouter_arc('A','D')
    G_1.ajouter_arc('D','E')
    G_1.ajouter_arc('E','B')
    G_1.ajouter_arc('B','C')
    G_1.ajouter_arc('C','E')
    G_1.ajouter_arc('C','F')
    G_1.ajouter_arc('G','C')
    print("parcours en largeur G_1 :",parcours_largeur(G_1, 'A'))
    print("parcours en largeur rec G_1 :",parcours_largeur_rec(G_1, 'A'))
    print()
#    print("parcours en largeur recursif G_1 :",parcours_profondeur_rec(G_1, 'A'))
    print()
    print("un chemin entre A et G ?",existe_chemin(G_1, 'A', 'G'))
    print("chemin de A à G",un_chemin(G_1,'A','G'))
    print("un chemin entre G et A ?",existe_chemin(G_1, 'G', 'A'))
    print("chemin de C à D",un_chemin(G_1,'C', 'D'))
    print("un chemin entre D et C ?",existe_chemin(G_1, 'D', 'C'))
    print("chemin de D à C",un_chemin(G_1,'D', 'C'))
    print("un chemin entre A et C ?",existe_chemin(G_1, 'A', 'C'))
    print("chemin de A à C",un_chemin(G_1,'A', 'C'))
 

 
    #creation de G_2
    G_2=Graphe()
    G_2.ajouter_arete('a','b')
    G_2.ajouter_arete('a','c')
    G_2.ajouter_arete('c','d')
    G_2.ajouter_arete('d','b')
    G_2.ajouter_arete('b','e')
    G_2.ajouter_arete('d','e')
    G_2.ajouter_arete('e','g')
    G_2.ajouter_arete('e','f')
    G_2.ajouter_arete('f','g')
    G_2.ajouter_arete('g','h')

    print("parcours en largeur G_2 :",parcours_largeur(G_2, 'g'))
    print("parcours en largeur rec G_2 :",parcours_largeur_rec(G_2, 'g'))
    print()
 #   print("parcours en largeur recursif G_2 :",parcours_largeur_rec2(G_2, 'g'))
    print()
  
    print("G_2 connexe ? (attendu oui) ",est_connexe(G_2))
    G_2.ajouter_arete('aa','bb')
    print("G_2 connexe ? (attendu non)",est_connexe(G_2))
    print("parcours_arcs de aa à bb",parcours_arcs(G_2,'aa'))
    print("chemin de aa à bb",un_chemin(G_2,'aa','bb'))
    print("chemin de a à h",un_chemin(G_2,'a','h'))
    print("chemin de a à a",un_chemin(G_2,'a','a'))
    print("chemin de c à h",un_chemin(G_2,'c','h'))


