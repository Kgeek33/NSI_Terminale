#exo 1
def liste_puissances(a,n):
    """prend en argument un nombre entier a, un entier strictement positif n
    et renvoie la liste de ses puissances d'exposants 1 à n"""
    puissances = []
    # première puissance (d'exposant 1)
    p=a
    for exposant in range (1,n+1):
        puissances.append(p)
        #puissance suivante
        p=p*a

    return puissances
        

def liste_puissances_borne(a,borne):
    """rend en arguments un nombre entier a supérieur ou égal à 2 et un entier borne,
    et renvoie la liste de ses puissances à partir de l'exposant 1,
    strictement inférieures à borne."""
    puissances = []
    # première puissance (d'exposant 1)
    p=a
    while p<borne:
        puissances.append(p)
        #puissance suivante
        p=p*a
    return puissances
    

assert liste_puissances(3, 5)==[3, 9, 27, 81, 243]
assert liste_puissances(-2, 4)==[-2, 4, -8, 16]
assert liste_puissances_borne(2, 16)==[2, 4, 8]
assert liste_puissances_borne(2, 17)==[2, 4, 8, 16]
assert liste_puissances_borne(5, 5)==[]

#exo 2
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def codes_parfait(mot):
    """Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene = ""
    code_additionne = 0 
    for c in mot:
        code_concatene = code_concatene +  str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    #construction du booléen mot_est_parfait
    mot_est_parfait = (code_concatene%code_additionne==0)
    return code_additionne, code_concatene, mot_est_parfait

assert codes_parfait("PAUL")==(50, 1612112, False)
assert codes_parfait("ALAIN")==(37, 1121914, True)
