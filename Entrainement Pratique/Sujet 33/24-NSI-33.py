def renverse(mot: str) -> str:
    a: str = ""
    for i in range(len(mot) - 1, -1, -1):
        a += mot[i]
    return a


assert renverse("") == ""
assert renverse("abc") == "cba"
assert renverse("informatique") == "euqitamrofni"


def crible(n: int) -> list[int]:
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers: list[int] = []
    tab: list[bool] = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple: int = 2
            while (multiple * i) < n:
                tab[multiple * i] = False
                multiple += 1
    return premiers


assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5) == [2, 3]
