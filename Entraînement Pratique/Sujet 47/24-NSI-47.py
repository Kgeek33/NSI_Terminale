def max_dico(dico: dict[str, int]):
    nom = None
    valeur = None

    for cle in dico:
        if nom is None and valeur is None:
            nom = cle
            valeur = dico[cle]
        else:
            if dico[cle] > valeur:
                nom = cle
                valeur = dico[cle]
    
    return (nom, valeur)



assert max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103,
                'Tim': 50}) == ('Ada', 201)
assert max_dico({'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50}) == (
    'Alan', 222) or ('Eve', 222)


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


def eval_expression(tab):
    p = Pile()
    for ... in tab:
        if element != '+' ... element != '*':
            p.empiler(...)
        else:
            if element == ...:
                resultat = ... + ...
            else:
                resultat = ...
            p.empiler(...)
    return ...
