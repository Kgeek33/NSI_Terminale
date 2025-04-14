d = {chr(i+ord('A')): chr((i+13) % 26+ord('A')) for i in range(26)}


def cesar_symetrique(s: str):
    num = 0
    chaine = ""
    while num < len(s):
        LAlettre = s[num]
        chaine += d[LAlettre]
        num += 1
    return chaine


if __name__ == "__main__":
    assert cesar_symetrique("N") == "A"
    assert cesar_symetrique("A") == "N"
