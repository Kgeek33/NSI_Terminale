from random import randint

compteur = 0


def generate_pyramide(h: int) -> list[list[int]]:
    UNEliste: list[list[int]] = []
    for i in range(1, h + 1):
        UNtableau = []
        for _ in range(i):
            UNtableau.append(randint(1, 9))
        UNEliste.append(UNtableau)
    return UNEliste


def afficher_pyramide(pyramide: list[list[int]]) -> None:
    for i in range(1, len(pyramide) + 1):
        texte = ""
        for _ in range(len(pyramide) - i):
            texte += " "
        for elm in pyramide[i - 1]:
            texte += str(elm)
            texte += " "
        print(texte)


def gain_max_rec(pyramide: list[list[int]]) -> int:
    if len(pyramide) == 1:
        return pyramide[0][0]
    gain_gauche = gain_max_rec([row[:-1] for row in pyramide[1:]])
    gain_droite = gain_max_rec([row[1:] for row in pyramide[1:]])
    return pyramide[0][0] + max(gain_gauche, gain_droite)


def gain_max_naif(pyramide: list[list[int]]) -> int:
    global compteur
    compteur += 1
    if len(pyramide) == 1:
        return pyramide[0][0]
    gain_gauche = []
    gain_droite = []
    for k in range(1, len(pyramide)):
        gain_gauche.append(pyramide[k][:-1])
    for k in range(1, len(pyramide)):
        gain_droite.append(pyramide[k][1:])
    return pyramide[0][0] + max(
        gain_max_naif(gain_gauche),
        gain_max_naif(gain_droite)
    )


def gain_max_memo(pyramide: list[list[int]], memo: dict) -> int:
    global compteur
    compteur += 1
    if len(pyramide) == 1:
        return pyramide[0][0]
    key = tuple(tuple(row) for row in pyramide)
    if key in memo:
        return memo[key]

    gain_gauche = gain_max_memo([row[:-1] for row in pyramide[1:]], memo)
    gain_droite = gain_max_memo([row[1:] for row in pyramide[1:]], memo)

    memo[key] = pyramide[0][0] + max(gain_gauche, gain_droite)
    return memo[key]


if __name__ == "__main__":
    p_1 = [[7], [3, 4], [8, 4, 9], [1, 9, 2, 3]]
    print("Pyramide p_1 :")
    afficher_pyramide(p_1)
    print("Gain maximum (récursif) :", gain_max_rec(p_1))
    print("Gain maximum (naïf) :", gain_max_naif(p_1))
    print("Gain maximum (mémoïsé) :", gain_max_memo(p_1, {}))
    print("Compteur :", compteur)
    print("--" * 30)

    compteur = 0
    pyramide = generate_pyramide(5)
    print("Pyramide générée :")
    afficher_pyramide(pyramide)
    print("Gain maximum (récursif) :", gain_max_rec(pyramide))
    print("Gain maximum (naïf) :", gain_max_naif(pyramide))
    print("Gain maximum (mémoïsé) :", gain_max_memo(pyramide, {}))
    print("Compteur :", compteur)
    print("--" * 30)

    compteur = 0
    p_2 = [
        [8],
        [8, 2],
        [1, 8, 6],
        [7, 8, 2, 5],
        [3, 4, 3, 6, 4],
        [6, 9, 1, 4, 6, 5],
        [5, 3, 2, 2, 7, 3, 2],
        [6, 3, 7, 1, 1, 5, 3, 2],
        [9, 5, 3, 2, 8, 4, 2, 4, 7],
        [6, 3, 4, 9, 4, 2, 9, 1, 7, 8]
    ]
    print("Pyramide p_2 :")
    afficher_pyramide(p_2)
    print("Gain maximum (récursif) :", gain_max_rec(p_2))
    print("Gain maximum (naïf) :", gain_max_naif(p_2))
    print("Gain maximum (mémoïsé) :", gain_max_memo(p_2, {}))
    print("Compteur :", compteur)
    print("--" * 30)
