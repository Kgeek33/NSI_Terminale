def estTrie(t: list[int]):
    """
    retourne True si le tableau t est trié dans l'ordre croissant
    False sinon
    >>> estTrie([17, 28, 39, 54, 59, 72])   #True
    >>> estTrie([17, 28, 9, 54, 59, 72])    #False
    >>> estTrie([1,1,1])                    #True
    >>> estTrie([])                         #True
    """
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            print("liste non triée")
            return False
    # print("liste triée")
    return True


def insere(t: list[int], i: int, v: int):
    """insère v dans t[0..i[ supposé trié"""
    j = i
    while j > 0 and t[j - 1] > v:
        t[j] = t[j - 1]
        print(t)
        j = j - 1
    t[j] = v


def tri_insertion(t: list[int]):
    """trie le tableau t dans l'ordre croissant"""
    print("debut de la boucle", "   0", t[:1], "-", t[1:])
    for i in range(1, len(t)):
        insere(t, i, t[i])
        print("fin de l'insertion no", i, t[:i+1], "-", t[i+1:])
        # invariant : t[0..i+1[ est trié
        assert estTrie(t[:i+1])
    # postcondition
    assert estTrie(t)


T = [72, 39, 28, 59, 17, 54]
tri_insertion(T)
print(T)

T = [61, 13, 5, 16, 17, 2]
tri_insertion(T)
print(T)
print()


def insere_naiss(h: list[tuple], i: int, v: tuple):
    """v est un tuple informaticien"""
    """insère v dans h[0..i[ supposé trié par naissances croissantes"""
    j = i
    while j > 0 and h[j - 1][1] > v[1]:
        h[j] = h[j - 1]
        print(h)
        j = j - 1
    h[j] = v


def tri_ins_naissance_cr(h: list[tuple]):
    """trie le tableau h dans l'ordre croissant des naissances"""
    print("debut de la boucle", "   0", h[:1], "-", h[1:])
    for i in range(1, len(h)):
        insere_naiss(h, i, h[i])
        print("fin de l'insertion no", i, h[:i+1], "-", h[i+1:])
        # invariant : h[0..i+1[ est trié
        # dans l'ordre des naissances croissantes

    # postcondition


def insere_deces(h: list[tuple], i: int, v: tuple):
    """v est un tuple informaticien"""
    """insère v dans h[0..i[ supposé trié par deces croissants"""
    "a completer"
    j = i
    while j > 0 and h[j - 1][2] < v[2]:
        h[j] = h[j + 1]
        print(h)
        j = j + 1
    h[j] = v


def tri_ins_deces_decr(h: list[tuple]):
    """trie le tableau t dans l'ordre croissant"""
    print("debut de la boucle", "   0", h[:1], "-", h[1:])
    for i in range(1, len(h)):
        insere_deces(h, i, h[i])
        print("fin de l'insertion no", i, h[:i+1], "-", h[i+1:])
        # invariant : h[0..i+1[ est trié dans l'ordre des deces croissants
    # postcondition


histoire = [('Jobs', 1955, 2011),
            ('Dijkstra', 1930, 2002),
            ('Turing', 1912, 1954),
            ('Hopper', 1906, 1992,)]

if __name__ == "__main__":

    print(histoire)

    # Question 1
    tri_ins_naissance_cr(histoire)

    # Question 2
    tri_ins_deces_decr(histoire)
    # print(histoire)
