from classe_noeud import Noeud
from parcours import (
    parcours_infixe,
    parcours_prefixe,
    parcours_postfixe,
    parcours_suffixe
)
from arbre_operations import est_feuille


def expression(a):
    """renvoie l'expression parenthésée sous forme de chaine de caractères"""
    if a is None:
        return ""
    e = parcours_infixe(a)

    return e


def evaluer(a: Noeud):
    """renvoie l'évaluation de l'expression décrite par l'arbre a"""
    if est_feuille(a):
        assert a.valeur() not in ["+", "-", "/"]
        res = a.valeur()
    elif a.valeur() == "+":
        res = evaluer(a.gauche()) + evaluer(a.droit())
    elif a.valeur() == "-":
        res = evaluer(a.gauche()) - evaluer(a.droit())
    elif a.valeur() == "/":
        res = evaluer(a.gauche()) / evaluer(a.droit())
    elif a.valeur() == "*":
        res = evaluer(a.gauche()) * evaluer(a.droit())
    elif a.valeur() == "^":
        res = evaluer(a.gauche()) ** evaluer(a.droit())
    else:
        raise ValueError("opérateur inattendu")
    return res


if __name__ == "__main__":
    def test(a):
        print("parcours infixe : ", end="")
        print(parcours_infixe(a))
        print()
        print("parcours prefixe : ", end="")
        print(parcours_prefixe(a))
        print()
        print("parcours postfixe : ", end="")
        print(parcours_postfixe(a))
        print()
        print("parcours suffixe : ", end="")
        print(parcours_suffixe(a))
        print()
        print("expression évaluée : ", end="")
        print(
            expression(a), "=", evaluer(a))

    A = Noeud('+',  Noeud(2, None, None), Noeud("/", Noeud(3, None, None),
              Noeud("-", Noeud(4, None, None), Noeud(7, None, None))))

    test(A)     # -> (2)+((3)/((4)-(7))) = 1

    B = Noeud('^', Noeud("+", Noeud(1.2, None, None), Noeud(6.8, None, None)),
              Noeud("+", Noeud(4, None, None), Noeud(-2, None, None)))
    test(B)     # -> (1.2+6.8)^(4+(-2)) = 64

    C = Noeud('**', Noeud("-", Noeud("*", -4, -2),
              Noeud(6, None, None)), Noeud("*", 5, 2))
    test(C)  # -> ((-4)*(-2)-6)**(5*2) =1024
