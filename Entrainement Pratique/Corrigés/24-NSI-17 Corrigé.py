#exo 1
def nb_repetitions(elt,tab):
    cpt=0
    for e in tab :
        if e==elt :
            cpt=cpt+1
    return cpt

assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5])==3
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R'])==2
assert nb_repetitions(12, [1, 3, 7, 21, 36, 44])==0


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
