# Créé le 20/09/2020 en Python 3.4

def cree():
    """crée et renvoie un dictionnaire vide"""
    # on renvoie une liste vide
    # pas de couple clé,valeur dedans à l'initialisation
    return []


def cle(d, k):
    """renvoie True si et seulement si le dictionnaire d contient la clé k"""
    # pour chaque couple (cle,valeur) de d ...
    for elt in d:
        # la clé est la premiere composante du couple (cle,valeur)
        if elt[0] == k:
            return True
    return False


def lit(d, k):
    """renvoie la valeur associée à la clé k dans le dictionnaire d ;
    et None si  la clé k n’apparait pas."""
    # pour chaque couple (cle,valeur) de d ...
    for elt in d:
        # si la clé est vaut k
        if elt[0] == k:
            # on renvoie la valeur
            return elt[1]
    # fin de parcours de d et clé introuvable
    raise KeyError("c pas possible ça...............................")


def ecrit(d, k, v):
    """ajoute au dictionnaire d l’association entre la clé k et la valeur v,
    en remplaçant une éventuelle association déjà présente par k."""

    # pour chaque couple (cle,valeur) de d ...
    for elt in d:
        # si la clé est vaut k
        if elt[0] == k:
            # on remplace la valeur
            elt[1] = v
    # fin de parcours de d et clé introuvable :
    # on ajoute le couple (clé,valeur)
    d.append([k, v])


if __name__ == '__main__':
    releve = cree()
    print("Tim est dedans ?", cle(releve, "Tim"))   # ->False

    ecrit(releve, "Tim", 13)
    print("Tim est dedans maintenant ?", cle(releve, "Tim"))   # ->True
    ecrit(releve, "Tom", 9)
    ecrit(releve, "Lou", 16)
    print("Bob est dedans ?", cle(releve, "Bob"))  # ->False
    print("Note de Bob : ", lit(releve, "Bob"))   # -> None
    print("Note de Tim : ", lit(releve, "Tim"))   # -> 13
    print("Note de Lou : ", lit(releve, "Lou"))   # -> 16
