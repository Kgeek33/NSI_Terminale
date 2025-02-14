#exo 1
def insertion_abr(a,cle):
    if a is None :
        return (None,cle,None)
    racine = a[1]
    sous_arbre_gauche=a[0]
    sous_arbre_droit=a[2]
    #Dans le cas ou cle est déjà présente dans a, renvoie l’arbre a inchange
    if cle == racine :
        return a
    # insertion à gauche
    if cle < racine :
        return (insertion_abr(sous_arbre_gauche,cle),racine,sous_arbre_droit)
    # insertion à droite
    if cle > racine :
        return (sous_arbre_gauche,racine,insertion_abr(sous_arbre_droit,cle))

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)
assert insertion_abr(abr1, 4)==((None,0,None),1,(None,2,(None,3,(None,4,None))))
assert insertion_abr(abr1, -5)==(((None,-5,None),0,None),1,(None,2,(None,3,None)))
assert insertion_abr(abr1, 2)==((None,0,None),1,(None,2,(None,3,None)))


#exo 2
def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    # nombre d'ojets
    n = len(liste_masses)
    #nb de boites remplies avec au moins un objet
    nb_boites = 0
    # masse totale par boite : on envisage le cas le pire avec autant de boites que d'objets
    boites = [ 0 for _ in range(n) ]
    # pour chaque objet
    for masse in liste_masses :
        # recherche d'une boite d'indice i
        i = 0
        # recherche dans les boites non vides d'une boite pouvant accueillir l'objet
        while i < nb_boites and boites[i] + masse > c: 
            i = i + 1
        
        if i == nb_boites:
            # impossible de choisir une boite non vide : besoin d'une boite de plus
            nb_boites=nb_boites+1
        boites[i] = boites[i] + masse 
    return nb_boites 

assert empaqueter([1, 2, 3, 4, 5], 10)==2
assert empaqueter([1, 2, 3, 4, 5], 5)==4
assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11)==5
