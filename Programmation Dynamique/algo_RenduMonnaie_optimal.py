import algo_RenduMonnaie_glouton as glouton


""" Rendu de monnaie"""

euros = (1, 2, 5, 10, 20, 50, 100, 200)

test_exo2 = False


def nb_rendu(pieces, s, prof=""):
    if s == 0:
        return 0
    if test_exo2:
        print(prof, "nb-rendu(", pieces, s, ")")
    nb_pieces_a_rendre = s  # s=1+1+1+...1 dans le pire des cas
    for p in pieces:
        if s-p >= 0:
            nb_pieces_a_rendre = min(
                nb_pieces_a_rendre, 1+nb_rendu(pieces, s-p, prof+" "))
    return nb_pieces_a_rendre


print(nb_rendu(euros, 4))

test = False
if __name__ == '__main__' and test:

    R_G = glouton.rendre_monnaie(euros, 12)
    print("rendu glouton 12 : ", R_G)
    nb_opt = nb_rendu(euros, 12)
    print("nb de pièces optimal pour rendre 12 :", nb_opt)
    # vérifie que le rendu glouton est le meilleur avec
    # les systeme de pièces de l'euro
    assert len(R_G) == nb_opt
    R_G = glouton.rendre_monnaie(euros, 18)
    print("rendu glouton 18 : ", R_G)
    nb_opt = nb_rendu(euros, 18)
    print("nb de pièces optimal pour rendre 18 :", nb_opt)
    # vérifie que le rendu glouton est le meilleur avec
    # les systeme de pièces de l'euro
    assert len(R_G) == nb_opt

    print("rendu glouton 8 avec (1,4,5) : ",
          glouton.rendre_monnaie((1, 4, 5), 8))
    print("nb de pièces optimal pour rendre 8 :", nb_rendu((1, 4, 5), 8))

    print("rendu glouton 4 avec (1,2,5) : ",
          glouton.rendre_monnaie((1, 2, 5), 4))
    print("nb de pièces optimal pour rendre 8 :", nb_rendu((1, 2, 5), 4))

    print("rendu glouton 29 en euros) : ", glouton.rendre_monnaie(euros, 29))
    print("nb_rendu...")
    print("nb de pièces optimal pour rendre 29 :", nb_rendu(euros, 29))
