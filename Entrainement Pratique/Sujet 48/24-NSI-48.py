def voisins_entrants(adj: list, x: int) -> list:
    list_voisin = []
    for i in range(len(adj)):
        if x in adj[i]:
            list_voisin.append(i)
    return list_voisin

assert voisins_entrants([[1, 2], [2], [0], [0]], 0) == [2, 3]
assert  voisins_entrants([[1, 2], [2], [0], [0]], 1) == [0]


def nombre_suivant(s: str) -> str:
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += str(compte) + s[i] 
            chiffre = s[i] 
            compte = 1 
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat


assert nombre_suivant("1211") == "111221"
assert nombre_suivant("311") == "1321"
