d = {chr(i+ord('A')): chr((i+13) % 26+ord('A')) for i in range(26)}
# les espaces et les apostrohes ne sont cryptés
d[' '] = ' '
d["'"] = "'"
print(d)


# chiffrement cesar
def chiffre_cesar(msg):
    msg_chiffre = ''
    desaccents = {'é': 'e', 'è': 'e', 'ê': 'e', 'à': 'a', 'ù': 'u', 'ç': 'c'}
    for c_accent in desaccents:
        msg = msg.replace(c_accent, desaccents[c_accent])
    msg = msg.upper()
    for c in msg:
        # concaténation avec le caractère crypté
        msg_chiffre = msg_chiffre+d[c]
    return msg_chiffre


print(chiffre_cesar("cyber cesar"))
print(chiffre_cesar(chiffre_cesar("cyber cesar")))

# chiffrement xor


def unicode(s: str):
    return (
        [ord(c) for c in s],
        [bin(ord(c)) for c in s],
        [hex(ord(c)) for c in s]
    )


message = "logiciel"
u_dec, u_bin, u_hex = unicode(message)
print("unicode (decimal) de '{}' : {}".format(message, u_dec))
print("unicode (binaire) de '{}' : {}".format(message, u_bin))
print("unicode (hexa) de '{}' : {}".format(message, u_hex))
clef = "nsi"
u_dec, u_bin, u_hex = unicode(clef)
print("unicode (decimal) de '{}' : {}".format(clef, u_dec))
print("unicode (binaire) de '{}' : {}".format(clef, u_bin))
print("unicode (hexa) de '{}' : {}".format(clef, u_hex))


def chiffre_xor(msg: str, cle: str):
    """prend les chaines msg et clé en paramètres et
    renvoie la chaine des octets en hexa du message chiffré et
    la liste de leur codage unicode (en decimal) """
    UNEliste = []
    UNite = 0
    for i in range(len(msg)):
        if i == len(cle):
            i = 0
        caracMsg = msg[UNite]
        caracCle = cle[i]
        xOR = caracMsg ^ caracCle
        UNEliste.append(xOR)
        UNite += 1
    return UNEliste, "a completer"


message = "logiciel étoilé"
u_dec, u_bin, u_hex = unicode(message)
print("unicode (decimal) de '{}' : {}".format(message, u_dec))
print("unicode (binaire) de '{}' : {}".format(message, u_bin))
print("unicode (hexa) de '{}' : {}".format(message, u_hex))
clef = "nsi"
u_dec, u_bin, u_hex = unicode(clef)
print("unicode (decimal) de '{}' : {}".format(clef, u_dec))
print("unicode (binaire) de '{}' : {}".format(clef, u_bin))
print("unicode (hexa) de '{}' : {}".format(clef, u_hex))
print("message chiffré : {}".format(chiffre_xor(message, clef)[0]))
print("message chiffré (en decimal): {}".format(chiffre_xor(message, clef)[1]))


def dechiffre_xor(msg_decimal, cle):
    """prend la liste msg_decimal
    (liste des entiers codages unicode du msg chiffré)
    et la clé en paramètres et renvoie la chaine du message déchiffré """
    "à compléter"
    return "à compléter"


print("message déchiffré : {}".format(
    dechiffre_xor(chiffre_xor(message, clef)[1], clef)))
