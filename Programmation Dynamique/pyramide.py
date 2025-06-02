from random import randint


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
    if len(pyramide) == 1:
        return pyramide[0][0]
    gain_max = 0
    for i in range(len(pyramide[1])):
        gain = pyramide[0][0] + gain_max_naif([row[i:] for row in pyramide[1:]])
        gain_max = max(gain_max, gain)
    return gain_max


if __name__ == "__main__":
    pyramide = generate_pyramide(5)
    p_1 = [[7], [3, 4], [8, 4, 9], [1, 9, 2, 3]]
    print("Pyramide p_1 :")
    afficher_pyramide(p_1)
    print("Gain maximum (récursif) :", gain_max_rec(p_1))
    print("--" * 30)
    print("Pyramide générée :")
    afficher_pyramide(pyramide)
    print("Gain maximum (récursif) :", gain_max_rec(pyramide))
