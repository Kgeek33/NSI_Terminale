from random import randint


def generate_pyramide(h: int) -> list[list[int]]:
    UNEliste: list[list[int]] = []
    for i in range(1, h + 1):
        UNtableau = []
        for _ in range(i):
            UNtableau.append(randint(1, 9))
        UNEliste.append(UNtableau)
    return UNEliste


if __name__ == "__main__":
    print(generate_pyramide(5))
