#exo 1
def recherche(tab, n):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    n : nombre entier
    La fonction renvoie l'indice correspondant à n s’il est dans le tableau,
    None sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2 
        if n == tab[m]:
            return m 
        if n > tab[m]:
            debut = m + 1
        else:
            fin = m-1 
    return None


assert recherche([2, 3, 4, 5, 6], 5)==3
assert recherche([2, 3, 4, 6, 7], 5)==None 
assert recherche([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)==6
assert recherche([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)==None

#exo 2
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    '''Renvoie la position de la lettre dans l'alphabet'''
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    '''Renvoie le message codé par la méthode de César
    pour le decalage donné'''
    resultat = ''
    for car in message: 
        if 'A' <= car and car <= 'Z':
            indice = (position_alphabet(car)+decalage) % 26 
            resultat = resultat + ALPHABET[indice]
        else: # on ne code pas le caractere
            resultat = resultat + car 
    return resultat


assert cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4)=='FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
assert cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)=='BONJOUR A TOUS. VIVE LA MATIERE NSI !'