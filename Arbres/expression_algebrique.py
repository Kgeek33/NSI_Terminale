from classe_noeud import Noeud
from parcours import (
    parcours_infixe,
    parcours_prefixe,
    parcours_postfixe,
    parcours_suffixe
)
from arbre_operations import est_feuille


def expression(a):
    """renvoie l"expression parenthésée sous forme de chaine de caractères"""
    if a is None:
        return ""
    # une version développée
# e="("
# e=e+expression(a.gauche())
# e=e+str(a.valeur())
# e=e+expression(a.droit())
# e=e+")"
    # version formatée
    if est_feuille(a):
        e = "({})".format(a.valeur())
    else:
        e = "({}{}{})".format(expression(a.gauche()),
                              a.valeur(), expression(a.droit()))
    return e


def evaluer(a):
    """renvoie l"évaluation de l"expression décrite par l"arbre a"""
    if est_feuille(a):
        res = a.valeur()
    elif a.valeur() == "+":
        res = evaluer(a.gauche())+evaluer(a.droit())
    elif a.valeur() == "-":
        res = evaluer(a.gauche())-evaluer(a.droit())
    elif a.valeur() == "*":
        res = evaluer(a.gauche())*evaluer(a.droit())
    elif a.valeur() == "/":
        res = evaluer(a.gauche())/evaluer(a.droit())
    elif a.valeur() == "**" or a.valeur() == "^":
        res = evaluer(a.gauche())**evaluer(a.droit())
    elif a.valeur() == "%":
        res = evaluer(a.gauche()) % evaluer(a.droit())
    elif a.valeur() == "//":
        res = evaluer(a.gauche())//evaluer(a.droit())
    else:
        raise ValueError("opérateur inattendu")
    return res


if __name__ == "__main__":

    def test(a):
        print("parcours infixe : ", end="")
        parcours_infixe(a)
        print()
        print("parcours prefixe : ", end="")
        parcours_prefixe(a)
        print()
        print("parcours postfixe : ", end="")
        parcours_postfixe(a)
        print()
        print("parcours suffixe : ", end="")
        parcours_suffixe(a)
        print()
        print("expression évaluée : ", end="")
        print(expression(a), "=", evaluer(a))

    A = Noeud("+",  Noeud(2, None, None),
              Noeud("/",
                    Noeud(3, None, None),
                    Noeud("-", Noeud(4, None, None), Noeud(7, None, None))))

    test(A)     # -> (2)+((3)/((4)-(7))) = 1

    B = Noeud("^",
              Noeud("+",
                    Noeud(1.2, None, None),
                    Noeud(6.8, None, None)
                    ),
              Noeud("+",
                    Noeud(4, None, None),
                    Noeud(-2, None, None)
                    ))
    test(B)     # -> (1.2+6.8)^(4+(-2)) = 64

    C = Noeud("**",
              Noeud("-",
                    Noeud("*",
                          Noeud(-4, None, None),
                          Noeud(-2, None, None)
                          ),
                    Noeud(6, None, None)
                    ),
              Noeud("*",
                    Noeud(5, None, None),
                    Noeud(2, None, None)
                    ))
    test(C)  # -> ((-4)*(-2)-6)**(5*2) =1024
