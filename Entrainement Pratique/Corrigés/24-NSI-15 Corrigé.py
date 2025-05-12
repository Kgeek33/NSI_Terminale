#exo 1
def moyenne(tab):
    """prend en paramètre un tableau tab non vide de nombres
    flottants et qui renvoie la moyenne des valeurs du tableau.
    Les tableaux sont représentés sous forme de liste Python."""
    # precondition : tableau non vide
    assert len(tab)!=0
    #initialisation de la somme des elements à calculer
    somme=0
    for elt in tab:
        somme=somme+elt
    return somme/len(tab)
    

assert moyenne([1.0])==1.0
assert moyenne([1.0, 2.0, 4.0])==2.3333333333333335


#exo 2
def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    #initialisation de la chaine à retourner
    bin_a = ''
    # tant que le quotient de l'algo des divisions n'est pas nul
    while a!=0 :
        # le dernier reste obtenu vient en premièreposition de la chaine
        bin_a = str(a%2) + bin_a
        # nouvelle division
        a = a//2 
    return bin_a


assert binaire(83)=='1010011'
assert binaire(6)=='110'
assert binaire(127)=='1111111'
assert binaire(0)=='0'