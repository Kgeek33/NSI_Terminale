def traduire_romain(nombre):
    """ Renvoie l'écriture décimale du nombre donné en chiffres
    romains """
    romains = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    i = 0
    while i < len(nombre):
        if i + 1 < len(nombre) and romains[nombre[i]] < romains[nombre[i + 1]]:
            total += romains[nombre[i + 1]] - romains[nombre[i]]
            i += 2
        else:
            total += romains[nombre[i]]
            i += 1
    return total


assert traduire_romain("XIV") == 14
assert traduire_romain("XVII") == 17
assert traduire_romain("XIX") == 19
assert traduire_romain("XX") == 20
assert traduire_romain("XXI") == 21
assert traduire_romain("XXV") == 25
assert traduire_romain("XXIX") == 29
assert traduire_romain("XXX") == 30


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


assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6])
assert fusion([], []) == []
assert fusion([1, 2, 3], [])
