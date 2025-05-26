#exo 1
def voisins_entrants(adj, x):
    vois = []
    for i in range(len(adj)):
        if x in adj[i]:
            vois.append(i)
    return vois

assert voisins_entrants([[1, 2], [2], [0], [0]], 0)==[2, 3]
assert voisins_entrants([[1, 2], [2], [0], [0]], 1)==[0]


#exo 2
def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)): 
        if s[i] == chiffre:
            #compte la longueur d'un segment de chiffres egaux à s[i]
            compte = compte + 1 
        else:
            #fin de segment de chiffres égaux
            resultat += str(compte) + chiffre
            # réinititialisation pour la recherche du segment suivant ...
            chiffre = s[i] 
            compte = 1
    #fin du dernier segment de chiffres égaux
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat

assert nombre_suivant('1211')=='111221'
assert nombre_suivant('311')=='1321'

