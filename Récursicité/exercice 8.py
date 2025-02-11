import math


def nombre_de_chiffres(n):
    # Solution 1 : return len(str(n))
    # Solution 2 : return len(list(n))
    # Solution 3 :
    if n < 10:
        return 1

    return nombre_de_chiffres(n // 10) + 1


assert nombre_de_chiffres(34126) == 5
assert nombre_de_chiffres(math.floor(-10)) == 2
