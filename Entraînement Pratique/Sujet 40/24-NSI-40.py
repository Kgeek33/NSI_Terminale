animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},{'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},{'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},{'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},{'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]



def trouver_intrus(tab, g, d):
    """Renvoie la valeur de l'intrus situé entre les indices g et d 
    dans le tableau tab où :
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3."""
    if g == d:
        return ...
    else:
        nombre_de_triplets = (d - g) // ...
        indice = g + 3 * (nombre_de_triplets // 2)
        if ...:
            return ...
        else:
            return ...


assert trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7, 2,
                      2, 2, 4, 4, 4, 8, 8, 8], 0, 18) == 7
assert trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3], 0, 12) == 8
assert trouver_intrus([5, 5, 5, 1, 1, 1, 0, 0, 0, 6,
                      6, 6, 3, 8, 8, 8], 0, 15) == 3
