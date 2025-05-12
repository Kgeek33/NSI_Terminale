#exo 1
def moyenne(note):
    """prend en paramètre une liste notes non vide de tuples à deux éléments entiers
    de la forme (note, coefficient) (int ou float) positifs ou nuls ;
    et renvoie la moyenne pondérée des notes de la liste sous forme de flottant si la
    somme des coefficients est non nulle, None sinon."""
    #precondition sur le parametre note
    assert len(note)!=0
    somme_coeff=0
    somme=0
    for n in note :
        somme= somme + n[0]*n[1]
        somme_coeff=somme_coeff+ n[1]
    if somme_coeff != 0 :
        return somme/somme_coeff
    
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)])==9.142857142857142
assert moyenne([(3, 0), (5, 0)])==None


#exo 2
coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par 
        des "*" , les 0 par un espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
       liste_depart'''
    liste_zoomee = [] 
    for elt in liste_depart : 
        for i in range(k):
            liste_zoomee.append(elt)
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois 
       ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne,k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee) 
    return grille_zoomee

affiche(coeur)
affiche(dessin_zoom(coeur,2))
assert liste_zoom([1,2,3],3)==[1, 1, 1, 2, 2, 2, 3, 3, 3]
