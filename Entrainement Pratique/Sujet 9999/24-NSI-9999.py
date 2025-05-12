class Pile:
    """Classe définissant une structure de pile."""

    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()


def parentheses_correctes(expression: str) -> bool:
    """Renvoie un booléen indiquant si la chaîne ch
    est bien parenthésée"""
    p = Pile()
    for c in expression:
        if c == "(" or c == "[" or c == "{":
            p.empiler(c)
        elif c == ")" or c == "]" or c == "}":
            if p.est_vide():
                return False
            else:
                Enleve = p.depiler()
                match c:
                    case ")":
                        if Enleve != "(":
                            return False
                    case "]":
                        if Enleve != "[":
                            return False
                    case "}":
                        if Enleve != "{":
                            return False
    return p.est_vide()


assert parentheses_correctes("[(x)+(y)]/{2*a-sin(x)}") is True
assert parentheses_correctes("[-(b)+sqrt(b**2-4*(a*c)])/(2*a)") is False
