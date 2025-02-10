# tri par insertion

def insere(t, i, v):
    """insère v dans t[0..i[ supposé trié"""
    j = i
    while j > 0 and t[j - 1] > v:
        t[j] = t[j - 1]
        #print(t)
        j = j - 1
    t[j] = v

def tri_insertion(t):
    """trie le tableau t dans l'ordre croissant"""
    #print("debut de la boucle","   0",t[:1],"-",t[1:])
    for i in range(1, len(t)):
        insere(t, i, t[i])
        #print("fin de l'insertion no",i,t[:i+1],"-",t[i+1:])
        # invariant : t[0..i+1[ est trié
        #assert estTrie(t[:i+1])
    #postcondition
    #assert estTrie(t)

if __name__ == '__main__' :
    T=[72, 39, 28, 59, 17, 54]
    tri_insertion(T)
    print(T)

    T=[61, 13, 5, 16, 17, 2]
    tri_insertion(T)
    print(T)
    print()

