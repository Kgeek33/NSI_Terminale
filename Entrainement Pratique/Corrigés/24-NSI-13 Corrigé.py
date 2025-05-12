# exo 1
def recherche(elt,tab):
    """prend en paramètres elt un nombre entier et tab un
    tableau de nombres entiers (type list), et renvoie l’indice de la première occurrence
    de elt dans tab si elt est dans tab et None sinon."""
    for k  in range(len(tab)) :
        if tab[k]==elt:
            return k


assert recherche(1, [2, 3, 4]) ==None
assert recherche(1, [10, 12, 1, 56])==2
assert recherche(50, [1, 50, 1])==1
assert recherche(15, [8, 9, 10, 15])==3

#exo 2

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]:
        #fait reculer l'element en position i+1 sur la position i 
        tab_a[i] = tab_a[i+1]
        # fait avancer a à la position i+1
        tab_a[i+1] = a
        # position suivante
        i = i+1 
    return tab_a

assert insere([1, 2, 4, 5], 3)==[1, 2, 3, 4, 5]
assert insere([1, 2, 7, 12, 14, 25], 30)==[1, 2, 7, 12, 14, 25, 30]
assert insere([2, 3, 4], 1)==[1, 2, 3, 4]
assert insere([], 1)==[1]
