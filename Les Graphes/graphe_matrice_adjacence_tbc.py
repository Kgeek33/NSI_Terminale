class Graphe:
    """un graphe représenté par une matrice d'adjacence,
       où les sommets sont les entiers 0,1,...,n-1
       On ne traite pas les graphes pondérés ici :
       la matrice est une matrice de booléens qui désignent l'existence
       ou non d'une arête"""

    def __init__(self, n):
        """construit une matrice d'ordre n, représentant un graphe
        à n sommets sans arêtes"""
        self.adj = [[False for _ in range(n)] for _ in range(n)]

    def ajouter_arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie la matrice afin de créer un arc de s1 à s2"""
        self.adj[s1][s2] = True

    def arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        renvoie un booléen précisant l'existence ou non d'un arc de s1 à s2"""
        return self.adj[s1][s2]

    def ajouter_arete(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie la matrice afin de créer une arete de s1 à s2"""
        self.adj[s1][s2] = True
        self.adj[s2][s1] = True

    def voisins(self, s):
        """prend en parametre un sommet s et
        renvoie la liste de ses voisins
        (il existe une arc de s à chaque voisin)"""
        return [i for i in range(len(self.adj[s])) if self.adj[s][i]]

    def affiche(self):
        """affiche sur une ligne pour chaque sommet l'ensemble de ses voisins
        (dans un ordre indifférent)
        par ex :
        0 --> 1 3
        1 --> 2 3
        2 --> 3
        3 --> 1
        """
        for i in range(len(self.adj)):
            print(i, "-->", "".join(
                str(self.voisins(i))
            ))


def num(car: str):
    car_maj = car.upper()
    return (ord(car_maj)-ord('A'))


def crac(n: int):
    return chr(ord('A')+n)


if __name__ == "__main__":
    g = Graphe(4)
    g.ajouter_arete(0, 1)
    g.ajouter_arete(0, 3)
    g.ajouter_arete(1, 2)
    g.ajouter_arete(1, 3)
    g.ajouter_arete(2, 3)
    g.ajouter_arc(3, 1)
    g.affiche()
    print(g.arc(3, 1))
    g2 = Graphe(3)
    g2.ajouter_arete(0, 1)
    g2.ajouter_arete(1, 2)
    g2.affiche()

    g3 = Graphe(5)
    g3.ajouter_arete(0, 4)
    g3.ajouter_arete(2, 3)
    g3.affiche()
    g1_test = Graphe(8)
    g1_test.ajouter_arete(0, 1)
    g1_test.ajouter_arete(0, 2)
    g1_test.ajouter_arete(1, 3)
    g1_test.ajouter_arete(2, 3)
    g1_test.ajouter_arete(1, 4)
    g1_test.ajouter_arete(3, 4)
    g1_test.ajouter_arete(4, 5)
    g1_test.ajouter_arete(4, 6)
    g1_test.ajouter_arete(5, 6)
    g1_test.ajouter_arete(6, 7)

    g2_test = Graphe(8)
    g2_test.ajouter_arc(num('A'), num('C'))
    g2_test.ajouter_arc(num('A'), num('D'))
    g2_test.ajouter_arc(num('B'), num('A'))
    g2_test.ajouter_arc(num('B'), num('F'))
    g2_test.ajouter_arc(num('B'), num('G'))
    g2_test.ajouter_arc(num('C'), num('A'))
    g2_test.ajouter_arc(num('D'), num('G'))
    g2_test.ajouter_arc(num('E'), num('B'))
    g2_test.ajouter_arc(num('E'), num('F'))
    g2_test.ajouter_arc(num('F'), num('E'))
    g2_test.ajouter_arc(num('G'), num('B'))
    g2_test.ajouter_arc(num('G'), num('D'))
    g2_test.affiche()
