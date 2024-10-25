# Créé le 21/08/2020 en Python 3.4


# 1 visu pile d'appels
"""visualiser l'arbre des appels et les états successifs de la pile"""


def factorielle(n):
    res = 1
    if n > 1:
        res = n * factorielle(n-1)
    return res


def factorielle_alt(n):
    res = 1
    if n > 1:
        prec = factorielle_alt(n-1)
        res = n * prec
    return res


le_resutat = factorielle(5)


def factorielle_catastrophique(n):
    """Pourquoi ce nom ?...."""
    res = 1
    if n > 1:
        prec = factorielle_catastrophique(n+1)
        res = n * prec
    return res


le_resutat = factorielle(5)


# 2 visu pile d'appels
"""visualiser l'arbre des appels et les états successifs de la pile"""


def palindrome(s):
    # print("en entrée :",s)
    if len(s) == 0:
        return True
    premier = s[0]
    dernier = s[-1]
    if premier != dernier:
        return False
    centre = s[1:-1]
    retour = palindrome(centre)
    return retour


le_resutat = palindrome("kayak")
# print(le_resutat)
assert le_resutat == True
le_resutat = palindrome("engageetgagne")
# print(le_resutat)
assert le_resutat == False
le_resutat = palindrome("engagelejeuquejelegagne")
assert le_resutat == True
# print(le_resutat)


# 3 visu pile d'appels
"""visualiser l'arbre des appels et les états successifs de la pile"""
