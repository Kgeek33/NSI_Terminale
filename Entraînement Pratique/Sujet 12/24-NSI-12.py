from random import randint


def tri_selection(tab: list[int]) -> None:
    for i in range(len(tab)):
        premier = tab[i]
        minimum = tab[i]
        indexmin = i
        for j in range(i, len(tab)):
            if tab[j] < minimum:
                minimum = tab[j]
                indexmin = j
        tab[i] = minimum
        tab[indexmin] = premier


tab = [1, 52, 6, -9, 12]
tri_selection(tab)
assert tab == [-9, 1, 6, 12, 52]


def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)
