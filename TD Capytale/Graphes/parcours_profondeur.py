from une_pile_avec_une_liste_chainee import *
from graphe_dictionnaire_adjacence import *

def parcours_profondeur(g,sommet):
    """prend un graphe g  et sommet, l'un de ses sommets, en parametre;
    renvoie la liste des sommets de g parcourus dans un parcours en profondeur"""
#    print("parcours_profondeur : ",end="")
    p=Pile()
    sommets_coches=[]
    p.empiler(sommet)
    while not p.est_vide():
        s=p.depiler()
        if s not in sommets_coches:
            sommets_coches.append(s)
#            print(s,end=" ")
        voisins=[y for y in g.voisins(s) if y not in sommets_coches]
        for v in voisins:
            p.empiler(v)
#    print()
    return sommets_coches

def parcours_profondeur_rec(g,sommet,sommets_coches=None):
    if sommets_coches==None : sommets_coches=[]
    if sommet not in sommets_coches:
            sommets_coches.append(sommet)
            print(sommet,end=" ") 
    for v in g.voisins(sommet) :
        if not v in sommets_coches :
            #print(v)
            parcours_profondeur_rec(g,v,sommets_coches)
    return sommets_coches


# exo 7
def existe_chemin(g, s, t):
    """existe-t-il un chemin de s à t ?"""
    return t in parcours_profondeur(g, s)

# exo 8 : graphes connexes
def est_oriente(g):
    for s in g.sommets():
        for t in g.sommets():
            if g.arc(s,t) and not g.arc(t,s) : return True
    return False

    
def est_connexe_noriente(g):
    """uniquement pour un graphe non orienté.
    on utilise la propriété suivante : le graphe est connexe s'il existe un chemin dans le graphe qui contient tous les sommets
    cad le parcours du graphe contient tous les sommets
    """
    assert not est_oriente(g)
    sommets=g.sommets()
    # dans un parcours chaque sommet ne peut apparaitre qu'une seule fois
    return len(sommets)==len(parcours_profondeur(g,sommets[0]))

def est_connexe(g):
    """
    on boucle sur les couples de sommmets en cherchant des chemins qui les relient
    """
    
    for s in g.sommets():
        for t in g.sommets():
            if not existe_chemin(g, s, t):
                print("pas de chemin entre {} et {}".format(s,t))
                return False
    return True

# exo 9 chemin entre deux sommets
def parcours_arcs(g,depart,arcs_coches=None):
    """renvoie le dictionnaire des arcs parcourus où la clé est l’extrémité de l’arc et la valeur est l’origine de l’arc"""
    # arcs_coches est le dictionnaire à construire à partir du sommet depart pour parcourir le graphe en profondeur 
    if arcs_coches==None : arcs_coches={depart:None}
    #print(arcs_coches)
    voisins=[y for y in g.voisins(depart)]
    for v in voisins :
        if not v in arcs_coches :
#            print(depart, "-->",v)
            arcs_coches[v]=depart
            parcours_arcs(g,v,arcs_coches)
    return arcs_coches

from random import *
def parcours_arcs_prof_random(g,sommet):
    """prend un graphe g  et sommet, l'un de ses sommets, en parametre;
    renvoie la liste des sommets de g parcourus dans un parcours en profondeur"""
#    print("parcours_profondeur : ",end="")
    arcs_coches={sommet:None}
    p=Pile()
    sommets_coches=[]
    p.empiler(sommet)
    while not p.est_vide():
        s=p.depiler()
        if s not in sommets_coches:
            sommets_coches.append(s)

#            print(s,end=" ")
        voisins=[y for y in g.voisins(s) if y not in sommets_coches]
#        shuffle(voisins)
        for v in voisins:
            arcs_coches[v]=s
            p.empiler(v)
#    print()
    return arcs_coches



def un_chemin(g,depart,arrivee):
    """ prend en paramètre le graphe, les sommets de depart et d’arrivée,
    et renvoie un chemin sous forme de liste des sommets qui le constituent """
    ch=[]
    #construit le dictionnaire des arcs du parcours à partir du depart
    arcs=parcours_arcs(g,depart)
#    print("en profondeur",arcs)
    # reconstitue le chemin à faire
    # si l'arrivée n'apparait pas dans le parcours en profondeur, il n'y a pas de chemin depart-arrivée
    if not arrivee in arcs.keys(): return None
    # sinon on construit à reculons la liste des sommets à parcourir du départ vers l'arrivée
    s=arrivee
    while s != None:
        ch=[s]+ch
        s=arcs[s]
    return ch


if __name__ == '__main__' :
    
    #creation de G_1
    G_1=Graphe()
    G_1.ajouter_arc('A','B')
    G_1.ajouter_arc('C','E')
    G_1.ajouter_arc('C','F')
    G_1.ajouter_arc('A','D')
    G_1.ajouter_arc('D','E')
    G_1.ajouter_arc('E','B')
    G_1.ajouter_arc('B','C')
    G_1.ajouter_arc('G','C')
    print("G_1 orienté ? (attendu oui)",est_oriente(G_1))
    print("parcours en profondeur G_1 :",parcours_profondeur(G_1, 'A'))
    print()
    print("parcours en profondeur recursif G_1 :",parcours_profondeur_rec(G_1, 'A'))
    print()
    print("un chemin entre A et G ?",existe_chemin(G_1, 'A', 'G'))
    print("chemin de A à G",un_chemin(G_1,'A','G'))
    print("un chemin entre G et A ?",existe_chemin(G_1, 'G', 'A'))
    print("chemin de G à A",un_chemin(G_1,'G','A'))
    print("un chemin entre C et D ?",existe_chemin(G_1, 'C', 'D'))
    print("chemin de C à D",un_chemin(G_1,'C', 'D'))
    print("un chemin entre D et C ?",existe_chemin(G_1, 'D', 'C'))
    print("chemin de D à C",un_chemin(G_1,'D', 'C'))
    print("un chemin entre A et C ?",existe_chemin(G_1, 'A', 'C'))
    print("chemin de A à C",un_chemin(G_1,'A', 'C'))
 
    print("G_1 connexe ? (attendu non) ",est_connexe(G_1))
#     G_1.ajouter_arc('C','G')
#     print("G_1 connexe ? (attendu non)",est_connexe_oriente(G_1))

 
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

    print("G_2 orienté ? (attendu non)",est_oriente(G_2))
    print("parcours en profondeur G_2 :",parcours_profondeur(G_2, 'g'))
    print()
    print("parcours en profondeur random G_2 :",parcours_arcs_prof_random(G_2, 'g'))
    print()
    print("parcours en profondeur recursif G_2 :",parcours_profondeur_rec(G_2, 'g'))
    print()
  
    print("G_2 connexe ? (attendu oui) ",est_connexe_noriente(G_2))
    G_2.ajouter_arete('aa','bb')
    print("G_2 connexe ? (attendu non) ",est_connexe_noriente(G_2))
    print("parcours_arcs de aa à bb",parcours_arcs(G_2,'aa'))
    print("chemin de aa à bb",un_chemin(G_2,'aa','bb'))
    print("chemin de a à h",un_chemin(G_2,'a','h'))
    print("chemin de a à a",un_chemin(G_2,'a','a'))

    print("chemin de c à h",un_chemin(G_2,'c','h'))
