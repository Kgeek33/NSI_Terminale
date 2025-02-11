def exercice4():
    def estTrie(t):
        for i in range(len(t)-1):
            if t[i] > t[i+1]:
                print("listenontriée")
                return False
        # print("listetriée")
        return True

    assert estTrie([17, 28, 39, 54, 59, 72]) is True
    assert estTrie([17, 28, 9, 54, 59, 72]) is False
    assert estTrie([1, 1, 1]) is True
    assert estTrie([]) is True

    def docstring():
        pass


def exercice2():
    def insere(t, i, v):
        """insère v dans t[0...i[ supposé trié"""
        j = i
        while j > 0 and t[j-1] > v:
            # 5 while j > 0 and t[j] > v:
            t[j] = t[j-1]
            j -= 1
        t[j] = v
        # 9 t[j] = 0

    def tri_insertion(t):
        """trie le tableau t dans l'ordre croissant"""
        for i in range(1, len(t)):
            insere(t, i, t[i])
        print(t)

    def occurrences(t):
        a = {}
        for i in range(len(t)):
            if t[i] in a:
                a[t[i]] += 1
            else:
                a[t[i]] = 1
        return a

    def estTrie(t):
        for i in range(len(t)-1):
            if t[i] > t[i+1]:
                print("listenontriée")
                return False
        # print("listetriée")
        return True

    assert occurrences([10, 8, 7, 12, 7, 6, 10, 10]) == {
        6: 1, 7: 2, 8: 1, 10: 3, 12: 1}

    def identiques(d1, d2):
        for i in d1:
            if i in d2 and d1[i] != d2[i]:
                return False
        return True
    assert identiques({1: 1, 2: 1, 3: 1}, {1: 1, 2: 1, 3: 1, 4: 1}) is False

    def test(t):
        a = occurrences(t)
        tri_insertion(t)
        b_verif = occurrences(t)
        if identiques(a, b_verif) is False:
            return False

        if estTrie(t) is False:
            return False
        return True

    if __name__ == '__main__':
        print(test([72, 39, 28, 59, 17, 54]))
        print(test([2]))
        print(test([]))


exercice2()
