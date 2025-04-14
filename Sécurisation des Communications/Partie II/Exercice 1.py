d = {chr(i+ord('A')): chr((i+13) % 26+ord('A')) for i in range(26)}


def cesar_symetrique(s: str):
    chaine = ""
    for num in s:
        chaine += d[num]
    return chaine


if __name__ == "__main__":
    assert cesar_symetrique("N") == "A"
    assert cesar_symetrique("A") == "N"
    assert cesar_symetrique("NSI") == "AFV"
    assert cesar_symetrique("SANDRO") == "FNAQEB"
