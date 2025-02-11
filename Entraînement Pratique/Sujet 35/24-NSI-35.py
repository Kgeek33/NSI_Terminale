def annee_temperature_minimale(tab1: list[float], tab2: list[int]):
    LEmin = tab1[0]
    LAnnee = tab2[0]
    for i in range(len(tab1)):
        if tab1[i] < LEmin:
            LEmin = tab1[i]
            LAnnee = tab2[i]

    return (LEmin, LAnnee)


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert annee_temperature_minimale(t_moy, annees) == (12.5, 2016)


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
    return chaine == inverse


def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre
    est un palindrome'''
    chaine = str(nbre)
    return est_palindrome(chaine)


assert inverse_chaine("bac") == "cab"
assert est_palindrome("NSI") is False
assert est_palindrome("ISN-NSI") is True
assert est_nbre_palindrome(214312) is False
assert est_nbre_palindrome(213312) is True
