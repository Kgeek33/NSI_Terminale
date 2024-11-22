def moyenne(tab: list) -> float:
    if len(tab) == 0:
        raise ValueError("P.E.K.K.A UNE LISTE VIDE ?????????????????????????")
    
    moyenne = 0
    for valeur in tab:
        moyenne += valeur
    moyenne /= len(tab)

    return moyenne

assert moyenne([5,3,8]) == 5.333333333333333
assert  moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
moyenne([])

def tri(tab: list[0 | 1]):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = ... # premier indice de la zone non triée 
    j = ... # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = ... 
        else:
            valeur = ... 
            tab[j] = ... 
            ...
            j = ... 


