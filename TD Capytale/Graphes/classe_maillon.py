class Maillon:

    def __init__(self, v, s):
        self._valeur = v
        self._suivant = s

    def __str__(self, chaine="|"):
        if self is None:
            return "| |"
        elif Maillon.est_vide(self._suivant):
            return chaine+str(self._valeur)+"|"
        else:
            return chaine+"{}->{}".format(self.valeur(), Maillon.__str__(self.suite(),""))

    # s'applique sur l'objet self
    def valeur(self):
        return self._valeur

    def suite(self):
        return self._suivant

    def est_vide(lst):
        return lst is None


# calcul de la longueur
# recursif
def taille_rec(lst):
    if lst is None:
        return 0
    else:
        return 1 + taille_rec(lst._suivant)


# avec une boucle
def taille_iter(lst):
    """renvoie la longueur de la liste lst"""
    n = 0
    maillon = lst     #adresse du premier maillon de la liste
    while maillon is not None:
        n += 1
        maillon = maillon.suite()
        # ou bien maillon = maillon._suivant
    return n


# accès au n-ieme element
# itératif
def nieme_element_iter(n, lst):
    """renvoie le n-ième élément de la liste lst
       les éléments sont numérotés à partir de 0"""
    k = 0
    maillon = lst     #adresse du premier maillon de la liste
    while k<n and maillon is not None:
        k += 1
        maillon = maillon.suite()
        # ou bien maillon = maillon._suivant
    return maillon.valeur()


# recursif
def nieme_element_rec(n, lst):
    """renvoie le n-ième élément de la liste lst
       les éléments sont numérotés à partir de 0"""
    if lst is None or n<0:
        raise IndexError("indice invalide")
    if n == 0:
        return lst._valeur
    else:
        return nieme_element_rec(n - 1, lst._suivant)


def inserer_fin(lst, v):
    """renvoie le n-ième élément de la liste lst
       les éléments sont numérotés à partir de 0"""
    m = Maillon(v, None)
    maillon = lst     # adresse du premier maillon de la liste
    while maillon._suivant is not None:
        maillon = maillon.suite()
        # ou bien maillon = maillon._suivant
    maillon._suivant = m
    return lst


def concatener(lst1, lst2):
    """concatène les listes lst1 et lst2,
       sous la forme d'une nouvelle liste"""
    if lst1 is None:
        return lst2
    else:
        return Maillon(lst1._valeur, concatener(lst1._suivant, lst2))


def renverser(lst):
    """renvoie une nouvelle liste inversion de la liste lst
    renverser (None) renvoie  None
    renverser [30] renvoie   [30]
    renverser [3, 6, 9, 100] renvoie  [100, 9, 6, 3]
    """
    maillon = lst     # adresse du premier maillon de la liste
    rev_lst = None    # liste vide
    while maillon is not None:
        rev_lst = Maillon(maillon._valeur, rev_lst)
        maillon = maillon.suite()
        # ou bien maillon = maillon._suivant
    return rev_lst


def maximum(self):
    if self is self.liste_vide:
        return None
    elif self._suivant is self.liste_vide: 
        return self._valeur
    else: 
        return max(self._valeur, self._suivant.maximum())


def minimum(self):
    if self is self.liste_vide:
        return None
    elif self._suivant is self.liste_vide:
        return self._valeur
    else:
        return min(self._valeur, self._suivant.minimum())


def inserer_rec(x, lst):
    """prend en argument un entier x et une liste d’entier lst ,
    supposée triée dans l’ordre croissant et renvoie une nouvelle liste
    dans laquelle x a été inséré à sa place
    si lst est la liste lst contient dans cet ordre  1,2,5,8
    insérer_rec(3,lst) contient dans cet ordre  1,2,3,5,8"""

if __name__ == '__main__' :

    #creation avec la valeur 3 et une sous liste vide
    L1 = Maillon(30, None)
    print(L1) # <__main__.Maillon object at 0x...>
    print(L1.valeur()) # 3
    print(Maillon.est_vide(L1)) # False
    print("lg (iter) de ",L1,":",taille_iter(L1))
    print("lg (recursif) de ",str(L1),taille_rec(L1))
    c1 = Maillon(9, None)
    c2 = Maillon(6, c1)
    L2 = Maillon(3, c2)
    print(L2.suite().valeur()) # 6
    print(Maillon.est_vide(L2.suite().suite().suite())) # True
    print(str(L2))
    print("lg (iter) de ",L2,":",taille_iter(L2))
    print("lg (recursif) de ",str(L2),taille_rec(L2))
    for i in range(taille_iter(L2)):
        print(i,"-eme element (recursif) :",nieme_element_rec(i, L2))
    #print(10,"-eme element (recursif) :",nieme_element_rec(10, L2))
    for i in range(taille_iter(L2)):
        print(i,"-eme element (itératif) :",nieme_element_iter(i, L2))

    print(str(inserer_fin(L2,100)))
    #!!!! inserer_fin() a modifié L2
    print(str(L2))

    print(str(concatener(L1,L2)))
    L3=renverser(None)
    print(str(None), "renversée : ",str(L3))
    L3=renverser(L1)
    print(str(L1), "renversée : ",str(L3))
    L3=renverser(L2)
    print(str(L2), "renversée : ",str(L3))

    ##print("max de",str(L2),"=",L2.maximum())
    ##print("min de",str(L2),"=",L2.minimum())
    ##L2 = Maillon(3, Maillon(12, Maillon(9, Maillon.liste_vide)))
    ##print("max de",str(L2),"=",L2.maximum())
    ##print("min de",str(L2),"=",L2.minimum())
    ##print("max de",str(L1),"=",L1.maximum())
    ##print("min de",str(L1),"=",L1.minimum())

