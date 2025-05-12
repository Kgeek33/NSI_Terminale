#exo 1
def verifie(tab):
    """prend en paramètre un tableau de valeurs numériques tab et
    renvoie True si ce tableau est trié dans l’ordre croissant, False sinon."""
    for k in range(len(tab)-1):
        if tab[k]>tab[k+1]:
            return False
    return True
    
    
    
assert verifie([0, 5, 8, 8, 9])==True
assert verifie([8, 12, 4])==False
assert verifie([-1, 4])==True
assert verifie([])==True
assert verifie([5])==True


#exo 2
def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    #initialisation à vide du dictionnaire à renvoyer
    resultat = {}
    # pour chaque bulletin à dépouiller
    for bulletin in urne:
        # si le nom du candidat figure dans résultat
        # (il est déjà apparu au cours du dépouilement)
        if bulletin in resultat :
            # on incrémente le score du candidat
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            # le candidat apparait pour la première fois au cours du dépouillement
            resultat[bulletin]=1
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    # pour chaque candidat (clé du dictionnaire election)
    for candidat in election:
        #si son score est supérieur au score max 
        if election[candidat] > nmax :
            # le score max devient son score
            nmax = election[candidat]
    # la liste des candidats dont le score est égal au score max
    liste_finale = [ nom for nom in election if election[nom]==nmax ] 
    return liste_finale 

assert depouille([ 'A', 'B', 'A' ])=={'A': 2, 'B': 1}
assert depouille([])=={}
election = depouille(['A', 'A', 'A', 'B', 'C','B', 'C', 'B', 'C', 'B'])
assert election=={'A': 3, 'B': 4, 'C': 3}
assert vainqueurs(election)==['B']
assert vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1})==['A', 'B']
