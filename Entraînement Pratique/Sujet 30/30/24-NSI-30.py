def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return ... 
    elif romains[nombre[0]] >= ...: 
        return romains[nombre[0]] + ... 
    else:
        return ... 


def fusion(tab1, tab2):
    i, j = 0, 0
    resultat = []
    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            resultat.append(tab1[i])
            i += 1
        else:
            resultat.append(tab2[j])
            j += 1
    while i < len(tab1):
        resultat.append(tab1[i])
        i += 1
    while j < len(tab2):
        resultat.append(tab2[j])
        j += 1
    return resultat


print(fusion([3, 5], [2, 5]))  # [2, 3, 5, 5]
print(fusion([-2, 4], [-3, 5, 10]))  # [-3, -2, 4, 5, 10]
print(fusion([4], [2, 6]))
print(fusion([], []))  # []
print(fusion([1, 2, 3], []))
