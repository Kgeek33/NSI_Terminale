#exo 1

def recherche_min(tab):
    """prend en paramètre un tableau de nombres tab,
    et renvoie l’indice de la première occurrence du minimum de ce tableau"""  
    v_min=tab[0] #valeur du minimum
    i_min=0      #indice du minimum
    for i in range(len(tab)):
        # l'inegalité stricte permet de ne retenir que la première occurrence
        # une inegalité large aurait permis de retenir la dernière occurrence
        if tab[i]<v_min :
            v_min=tab[i]
            i_min=i
    return i_min

assert recherche_min([5])==0
assert recherche_min([2, 4, 1])==2
assert recherche_min([5, 3, 2, 2, 4])==2
assert recherche_min([-1, -2, -3, -3])==2


#exo 2
def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab)-1
    while gauche < droite:
        if tab[gauche] == 0 :
            #on ne touche pas au tableau et
            #on resserre le tableau à traiter par la gauche
            gauche = gauche+1 
        else :
            #on permute les elements indicés par droite et gauche
            tab[gauche] = tab[droite] 
            tab[droite] = 1
            #on resserre le tableau à traiter par la droite       
            droite = droite-1 
    return tab

assert separe([1, 0, 1, 0, 1, 0, 1, 0])==[0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0])==[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
