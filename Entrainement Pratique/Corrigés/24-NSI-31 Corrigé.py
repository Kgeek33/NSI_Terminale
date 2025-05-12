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

#exo 2
def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2 
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1 
    return False



assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)==True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)==False

