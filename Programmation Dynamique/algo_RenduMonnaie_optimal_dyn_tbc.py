import algo_RenduMonnaie_glouton as glouton


""" Rendu de monnaie"""

euros = (1, 2, 5, 10, 20, 50, 100, 200)
print_appels = True
CPT = {}


def nb_rendu(pieces: tuple, s: int, prof: str | None = None):
    """prend en paramètre le systeme de pieces (tuple) et s, la somme à rendre
    renvoie la liste des pieces rendues"""

    if prof is None:
        prof = ""

    if print_appels:
        print(prof+str(s))
    # compteur d'appels
    CPT[s] += 1
    # cas de base : si la somme a rendre est nulle, elle necessite zero pieces
    if s == 0:
        return 0
    nb_pieces_a_rendre = s  # s=1+1+1+...1 dans le pire des cas
    # pour chaque piece possible rendue
    for p in pieces:
        if print_appels:
            print(prof+str(p), end="-")
        if s-p >= 0:
            # le min permet de reinitialiser le nb de pieces a  rendre
            nb_pieces_a_rendre = min(
                nb_pieces_a_rendre, 1+nb_rendu(pieces, s-p, prof+" "))
        # si p>s : on ne fait rien (la combinaison examinée échoue)
        if print_appels:
            print()
    return nb_pieces_a_rendre


def nb_rendu_memo(pieces: tuple, s: int, dico: dict[int, int] = {}):
    """prend en parametre le systeme de pieces (tuple) et s, la somme a rendre,
    et dico le dictionnaire des calculs dejà effectues
    (programmation dynamique)
    renvoie *la taille de* la liste optimale des pieces rendues"""

    # cas de base : si la somme a rendre est nulle, elle necessite zero pieces
    if s == 0:
        return 0
    # si le rendu est connu (deja dans le dico), on ne le recalcule pas
    # on retourne directement sa valeur
    if s in dico:
        return dico[s]
    nb_pieces_a_rendre = s  # s=1+1+1+...1 dans le pire des cas
    # pour chaque piece possible rendue
    for p in pieces:
        if s-p >= 0:
            # on determine le min entre le nb_pieces_a_rendre et
            # 1+nb_rendu(pieces,s-p) et on le stocke dans le dico
            dico[s] = min(
                nb_pieces_a_rendre,
                1 + nb_rendu_memo(pieces, s-p, dico)
            )
        # si p>s : on ne fait rien (la combinaison examinee echoue)
    return dico[s]


def nb_rendu_dyn(pieces: tuple, s: int):
    """prend en parametre le systeme de pieces (tuple) et s, la somme à rendre,
    et utilise tab un tableau dans lequel on enregistre
    les tailles des solutions optimales calculees iterativement
    renvoie la *taille de* la liste optimale des pieces rendues"""
    tab = [0]*(s+1)
    # allocation du tableau a la taille attendue et initialisation a  0.
    # tab[0] est donc juste.
    # pour chaque somme inferieure ou egale a  la somme s passee en argument
    for n in range(1, s+1):
        # à compléter...

        tab[n] = n  # 1+1+1+1...+1 (n fois)
        for p in pieces:
            if p <= n:
                tab[n] = min(tab[n], tab[n-p]+1)
                # L'appel recursif de la version memo est remplace
                # par un acces au tableau tab
    return tab[s]


def rendre_monnaie_dyn(pieces: tuple, s: int):
    """prend en parametre le systeme de pieces (tuple) et s, la somme à rendre,
    et utilise tab_solt un tableau dans lequel on enregistre
    les solutions optimales calculees iterativement
    renvoie la liste optimale des pieces rendues"""
    tab_nb = [0]*(s+1)  # tableau des nb de pieces rendues
    tab_solt = [[]]*(s+1)  # tableau des rendus monnaie optimaux
    # allocation du tableau Ã  la taille attendue et initialisation Ã  0.
    # tab[0] est donc juste.
    # pour chaque somme inferieure ou egale a  la somme s passee en argument
    for n in range(1, s+1):
        # à compléter...
        pass

    return tab_solt[s]


if __name__ == '__main__':
    print_appels = False
    CPT = [0]*30

    R_G = glouton.rendre_monnaie(euros, 12)
    print("rendu glouton 12 : ", R_G)
    nb_opt = nb_rendu_memo(euros, 12)
    print("nb de pieces optimal pour rendre 12 :", nb_opt)
    # vérifie que le rendu glouton est le meilleur
    # avec les systeme de pièces de l'euro
    assert len(R_G) == nb_opt
    R_G = glouton.rendre_monnaie(euros, 18)
    print("rendu glouton 18 : ", R_G)
    nb_opt = nb_rendu_memo(euros, 18)
    print("nb de pieces optimal pour rendre 18 :", nb_opt)
    # vérifie que le rendu glouton est le meilleur
    # *avec les systeme de pièces de l'euro
    # assert len(R_G) == nb_opt

    print("rendu glouton 8 avec (1,4,5) : ",
          glouton.rendre_monnaie((1, 4, 5), 8))
    print("nb de pieces optimal pour rendre 8 :", nb_rendu_memo((1, 4, 5), 8))
    # compteur d'appels recursifs
    print_appels = True
    print("rendu glouton 4 avec (1,2,5) : ",
          glouton.rendre_monnaie((1, 2, 5), 4))
    print("nb de pieces optimal pour rendre 8 :", nb_rendu_memo((1, 2, 5), 4))

    CPT = [0]*30
    print_appels = False
    print("rendu glouton 29 en euros : ", glouton.rendre_monnaie(euros, 29))
    print("nb_rendu ...")
    nb_opt = nb_rendu(euros, 29)
    print("nb de pieces optimal pour rendre 29 :", nb_opt)
    print(CPT)

    print_appels = False
    print("rendu glouton 29 en euros : ", glouton.rendre_monnaie(euros, 29))
    print("nb_rendu dynamique ...")
    nb_opt_memo = nb_rendu_memo(euros, 29)
    print("nb de pieces optimal pour rendre 29 :", nb_opt_memo)
    assert nb_opt_memo == nb_opt
