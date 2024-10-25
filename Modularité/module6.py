def cree():
    """crée et renvoie un dictionnaire vide"""
    return []


def cle(d, k):
    """renvoie True si et seulement si le dictionnaire d contient la clé k"""
    for i in d:
        if k in i:
            return True
    return False


def lit(d, k):
    """renvoie la valeur associée à la clé k dans le dictionnaire d ; et None si  la clé k n’apparait pas"""
    for j in range(len(d)):
        if d[j][0] == k:
            return d[j][1]
    return None


def ecrit(d, k, v):
    """ajoute au dictionnaire d l’association entre la clé k et la valeur v, en remplaçant une éventuelle association déjà présente par k."""
    if cle(d, k) == True:
        # if d[lit(d, k)][0] == k:
        #     d[lit(d, k)][1] = v
        for i in d:
            if i[0] == k:
                i[1] = v
    else:
        d.append([k, v])
    return


if __name__ == '__main__':
    releve = cree()
    print("Tim est dedans ?", cle(releve, "Tim"))   # ->False
    assert cle(releve, "Tim") == False

    ecrit(releve, "Tim", 13)
    print("Tim est dedans maintenant ?", cle(releve, "Tim"))  # ->True
    assert cle(releve, "Tim") == True

    ecrit(releve, "Tom", 9)
    ecrit(releve, "Lou", 16)
    print("Bob est dedans ?", cle(releve, "Bob"))  # ->False
    assert cle(releve, "Bob") == False

    print("Note de Bob : ", lit(releve, "Bob"))   # -> None
    assert lit(releve, "Bob") == None

    print("Note de Tim : ", lit(releve, "Tim"))   # -> 13
    assert lit(releve, "Tim") == 13

    print("Note de Lou : ", lit(releve, "Lou"))   # -> 16
    assert lit(releve, "Lou") == 16

    ecrit(releve, "Lou", 10)
    print("Note de Lou maintenant : ", lit(releve, "Lou"))   # -> 10
    assert lit(releve, "Lou") == 10
