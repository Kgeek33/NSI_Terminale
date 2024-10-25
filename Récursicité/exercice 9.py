def pgcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


assert pgcd(24, 60) == 12


def recur_pgcd(a, b):
    if b > 0:
        return recur_pgcd(b, a % b)
    
    return a

assert recur_pgcd(24, 60) == 12
