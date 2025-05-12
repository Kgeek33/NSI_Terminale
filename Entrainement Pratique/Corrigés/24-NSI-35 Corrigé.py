#exo 1
def annee_temperature_minimale(t_moy, annees):
    assert len(t_moy)!=0 and len(t_moy)==len(annees)
    
    t_min=t_moy[0]
    an_min=annees[0]
    for k in range(len(annees)):
        if t_moy[k]<t_min :
            t_min=t_moy[k]
            an_min=annees[k]
    return (t_min,an_min)

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert annee_temperature_minimale(t_moy, annees)==(12.5, 2016)

#exo 2
def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = "" 
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse==chaine 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine =  inverse_chaine(str(nbre))
    return est_palindrome(chaine)

assert inverse_chaine('bac')=='cab'
assert est_palindrome('NSI')==False
assert est_palindrome('ISN-NSI')==True
assert est_nbre_palindrome(214312)==False
assert est_nbre_palindrome(213312)==True

