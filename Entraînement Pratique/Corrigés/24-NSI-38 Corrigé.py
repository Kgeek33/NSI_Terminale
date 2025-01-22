#exo 1
def indices_maxi(tab):
    """prend en paramètre un tableau non vide de nombres entiers tab,
    représenté par une liste Python et qui renvoie un tuple (maxi, indices) où :
    • maxi est le plus grand élément du tableau tab ;
    • indices est une liste Python contenant les indices du tableau tab
    où apparaît ce plus grand élément."""
    val_max = tab[0]
    ind_max = []
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
    for i in range(len(tab)):
        if tab[i] == val_max:
            ind_max.append(i)
    return (val_max, ind_max)

#tests
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))	# -->(9, [3, 8])
print(indices_maxi([7]))	# -->(7, [0])
assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])==(9, [3, 8])
assert indices_maxi([7])==(7, [0])

#exo 2

def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = [] 
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = [] 
    while pile != []:
        elt = pile.pop() 
        if elt >= 0: 
            pile_positifs.append(elt)
    pile_positifs=renverse(pile_positifs)
    return pile_positifs 


#tests
print(renverse([1, 2, 3, 4, 5])) # --> [5, 4, 3, 2, 1]
print(renverse([5])) # -->[5]
print(renverse([])) # -->[]
print(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8])) # -->[0, 5, 4, 10, 9]
print(positifs([-2])) # -->[]

assert renverse([1, 2, 3, 4, 5])==[5, 4, 3, 2, 1]
assert renverse([5])==[5]
assert renverse([])==[]
assert positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8])==[0, 5, 4, 10, 9]
assert positifs([-2])==[]