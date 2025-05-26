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


if __name__ == "__main__":
    afficher_pyramide(generate_pyramide(5))
