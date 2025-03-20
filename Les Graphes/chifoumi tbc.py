from random import randint
# from une_file_avec_une_liste_chainée import *
from graphe_dictionnaire_adjacence_tbc import Graphe

g_chifoumi = Graphe()
verbe = {}
g_chifoumi.ajouter_arc("la Pierre", "les Ciseaux")
verbe[("la Pierre", "les Ciseaux")] = "casse"
g_chifoumi.ajouter_arc("les Ciseaux", "le Papier")
verbe[("les Ciseaux", "le Papier")] = "coupe"
g_chifoumi.ajouter_arc("le Papier", "la Pierre")
verbe[("le Papier", "la Pierre")] = "enveloppe"
g_chifoumi.ajouter_arc("Spock", "la Pierre")
verbe[("Spock", "la Pierre")] = "vaporise"
g_chifoumi.ajouter_arc("Spock", "les Ciseaux")
verbe[("Spock", "les Ciseaux")] = "écrabouille"
g_chifoumi.ajouter_arc("le Papier", "Spock")
verbe[("Spock", "la Pierre")] = "discrédite"
g_chifoumi.ajouter_arc("les Ciseaux", "Lézard")
verbe[("les Ciseaux", "Lézard")] = "décapite"
g_chifoumi.ajouter_arc("la Pierre", "Lézard")
verbe[("la Pierre", "Lézard")] = "écrase"
g_chifoumi.ajouter_arc("Lézard", "le Papier")
verbe[("Lézard", "le Papier")] = "mange"
g_chifoumi.ajouter_arc("Lézard", "Spock")
verbe[("Lézard", "Spock")] = "empoisonne"


def plus_fort(s1, s2):
    pass
    return "a completer"


def resultat(s1, s2):
    if plus_fort(s1, s2) != plus_fort(s2, s1):
        return plus_fort(s1, s2)
    return "nul"


choix = [s for s in g_chifoumi.sommets()]


def le_jeu():
    # initiailisation des scores
    ton_score = 0
    mon_score = 0
    # tant que personne n'est à 3 points
    while mon_score < 3 or ton_score < 3:
        # le joueur joue
        ta_main = str(input("ta main ? "))
        # ta_main n'est pas une main valide
        while ta_main not in choix:
            ta_main = str(input(" fais une main qui existe, stp : "))

        # la machine joue (sans tricher cad sans tenir compte de ta_main !)
        ma_main = choix[randint(0, len(choix)-1)]
        # arbitrage, affichages, calcul des scores à compléter....
        if resultat(ma_main, ta_main) is ma_main:
            mon_score += 1
        else:
            ton_score += 1
        # affichage du nouveau score
        print("ton score :", ton_score, "--- mon score :", mon_score)

    if mon_score < ton_score:
        # la machine a gagné
        print("perdu !")
    else:
        print("Gagné")


testing = True
if __name__ == "__main__" and testing:
    print(g_chifoumi.adj)
    s = "la Pierre"
    t = "les Ciseaux"
    print(s, "gagne contre", t, "?", plus_fort(s, t))
    s = "les Ciseaux"
    t = "la Pierre"
    print(s, "gagne contre", t, "?", plus_fort(s, t))
    s = "le Papier"
    t = "la Pierre"
    print(s, "gagne contre", t, "?", plus_fort(s, t))
    s = "la Pierre"
    t = "le Papier"
    print(s, "gagne contre", t, "?", plus_fort(s, t))
    s = "les Ciseaux"
    t = "le Papier"
    print(s, "gagne contre", t, "?", plus_fort(s, t))
    s = "le Papier"
    t = "les Ciseaux"
    print(s, "gagne contre", t, "?", plus_fort(s, t))

    for s in g_chifoumi.sommets():
        for t in g_chifoumi.sommets():
            print(s, "gagne contre", t, "?", plus_fort(s, t))
            print(resultat(s, t))

    for s in g_chifoumi.sommets():
        for t in g_chifoumi.sommets():
            if plus_fort(s, t):
                print(resultat(s, t))

# le_jeu()
