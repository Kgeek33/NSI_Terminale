#exo 2
def ajoute_dictionnaires(d1,d2):
    """prend en paramètres deux dictionnaires d1 et d2 dont les clés et les valeurs associées sont des nombres et
    renvoie le dictionnaire d défini de la façon suivante :
    • les clés de d sont celles de d1 et celles de d2 réunies ;
    • si une clé est présente dans les deux dictionnaires d1 et d2,
    sa valeur associée dans le dictionnaire d est la somme de ses valeurs dans les dictionnaires d1 et d2 ;
    • si une clé n’est présente que dans un des deux dictionnaires,
    sa valeur associée dans le dictionnaire d est la même que sa valeur dans le dictionnaire où elle est présente."""
    d={}
    #recopie de d1 dans d
    for k1 in d1: d[k1]=d1[k1]
    # ajoute les valeurs de d2     
    for k2 in d2 :
        if k2 in d :
            d[k2]=d[k2]+d2[k2]
        else:
            d[k2]=d2[k2]
    return d

assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11})=={1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11})=={2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {})=={1: 5, 2: 7}
    
    
#exo 1
from random import randint

def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0 
    while nombre_cases_vues < nombre_cases : 
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nombre_cases 
        if not cases_vues[case_en_cours]: 
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues+1
        n = n+1
        print(cases_vues)
    return n

nombre_coups()