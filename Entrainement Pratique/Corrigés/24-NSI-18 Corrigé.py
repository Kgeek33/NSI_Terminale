def multiplication(n1,n2):
    """prend en paramètres deux nombres entiers relatifs n1 et n2,
    renvoie le produit de ces deux nombres.
    Les seules opérations arithmétiques autorisées sont l’addition et la soustraction"""
    vabs_1=n1
    signe = 1
    if n1<0 :
        vabs_1=-n1
        signe=-signe
    vabs_2=n2
    if n2<0 :
        vabs_2=-n2
        signe=-signe
    produit = 0
    for k in range(vabs_2):
        produit = produit + vabs_1
    return signe*produit

#une version récursive
def multiplication_rec(n1, n2):
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    produit = 0
    for k in range(n2):
        produit = produit + n1
    return produit

assert multiplication(0,-3)==multiplication_rec(0,-3)==0
assert multiplication(-4,0)==multiplication_rec(-4,0)==0
assert multiplication(-4,3)==multiplication_rec(-4,3)==-12
assert multiplication(4,-3)==multiplication_rec(4,-3)==-12
assert multiplication(4,5)==multiplication_rec(4,5)==20
assert multiplication(-4,-5)==multiplication_rec(-4,-5)==20


def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    #condition d'arrêt de la récursivité (cas de base)
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x:
        # on cherche dans la moitié droite
        return chercher(tab, x, m+1 , j) 
    elif tab[m] > x:
        # on cherche dans la moitié gauche
        return chercher(tab, x, i , m-1) 
    else:
        return m 


assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 10)==None
assert chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)==None
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5)==4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5)==2

