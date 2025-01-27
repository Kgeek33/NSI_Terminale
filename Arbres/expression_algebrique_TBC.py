from classe_noeud import *
from parcours import *
from arbre_operations import est_feuille



def expression(a):
    """renvoie l'expression parenthésée sous forme de chaine de caractères"""
    if a is None:
        return ""
#à compléter

    return e



def evaluer(a) :
    """renvoie l'évaluation de l'expression décrite par l'arbre a"""
    if est_feuille(a) :
        res = ## à completer
    elif a.valeur()=='+' :
        res=## à completer
    elif a.valeur()=='-' :
        res=## à completer
    elif ## à completer


    else : raise ValueError("opérateur inattendu")
    return res



if __name__ == '__main__' :

    def test(a):
        print("parcours infixe : ",end="");parcours_infixe(a);print()
        print("parcours prefixe : ",end="");parcours_prefixe(a);print()
        print("parcours postfixe : ",end="");parcours_postfixe(a);print()
        print("parcours suffixe : ",end="");parcours_suffixe(a);print()
        print("expression évaluée : ",end="");print(expression(a),"=",evaluer(a))

    A=  Noeud('+',  Noeud(2,None,None),
                    ## à completer)

    test(A)     # -> (2)+((3)/((4)-(7))) = 1

    B = Noeud('^',## à completer)
    test(B)     # -> (1.2+6.8)^(4+(-2)) = 64

    C = Noeud('**',## à completer)
    test(C)     #  -> ((-4)*(-2)-6)**(5*2) =1024

