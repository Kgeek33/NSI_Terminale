#exo 1
def couples_consecutifs(tab):
    """prend en paramètre un tableau de nombres entiers tab non vide (type list),
    et renvoie la liste Python (éventuellement vide) des couples d’entiers consécutifs successifs
    qu’il peut y avoir dans tab"""
    #precondition
    assert len(tab)!=0
    res=[]
    for k in range(len(tab)-1):
        if tab[k+1]==tab[k]+1:
            # ajout du ***couple*** des deux valeurs consécutives
            res.append((tab[k],tab[k+1]))
    return res

assert couples_consecutifs([1, 4, 3, 5])==[]
assert couples_consecutifs([1, 4, 5, 3])==[(4, 5)]
assert couples_consecutifs([1, 1, 2, 4])==[(1, 2)]
assert couples_consecutifs([7, 1, 2, 5, 3, 4])==[(1, 2), (3, 4)]
assert couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7])==[(1, 2), (2, 3), (-5, -4)]

#exo 2
def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage à gauche
        colore_comp1(M, i-1, j, val)
    if i < len(M)-1: # propage à droite 
        colore_comp1(M, i+1, j, val) 
    if j >=0 : # propage en haut 
        colore_comp1(M, i, j-1, val) 
    if j<len(M[i])-1: # propage en bas 
        colore_comp1(M, i, j+1, val)


M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M==[[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]

