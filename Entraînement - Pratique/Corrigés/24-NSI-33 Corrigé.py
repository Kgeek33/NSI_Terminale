#exo 1
def renverse(mot):
    """prend en paramètre une chaîne de caractères mot et
    renvoie cette chaîne de caractères en ordre inverse"""
    a_l_envers=""
    for c in mot :
        a_l_envers=c+a_l_envers
    print(a_l_envers)
    return a_l_envers


assert renverse("")==""
assert renverse("abc")=="cba"
assert renverse("informatique")=="euqitamrofni"

#exo 2
def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i) 
            multiple = 2*i 
            while multiple < n:
                tab[multiple] = False 
                multiple = multiple+i
    print(premiers)
    return premiers

assert crible(40)==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5)==[2, 3]

