#exo 1
def taille(arbre,lettre):
    print(arbre[lettre][0])
    #cas de l'arbre feuille : 
    if arbre[lettre][0]=='' and arbre[lettre][1]=='':
        return 1
    if arbre[lettre][0]=='' :
        return 1+taille(arbre,arbre[lettre][1])
    if arbre[lettre][1]=='':
        return 1+taille(arbre,arbre[lettre][0])
    # 1 + taille du sous-arbre gauche + taille du sous-arbre droit
    return 1+taille(arbre,arbre[lettre][0])+taille(arbre,arbre[lettre][1])

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

assert taille(a, 'F')==9
assert taille(a, 'B')==5
assert taille(a, 'I')==2
#exo 2
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    # pour chaque dernier element de la partie triee a gauche 
    for k in range(N-1):
        #recherche de l'indice imin du minimum de la partie non triee a droite
        imin = k
        for i in range(imin, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin)
        print(tab)

tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)

assert tab==[6, 12, 18, 21, 25, 41, 55]
