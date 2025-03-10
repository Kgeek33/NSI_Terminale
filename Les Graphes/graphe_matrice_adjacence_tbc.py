class Graphe:
    """un graphe représenté par une matrice d'adjacence,
       où les sommets sont les entiers 0,1,...,n-1
       On ne traite pas les graphes pondérés ici :
       la matrice est une matrice de booléens qui désignent l'existence
       ou non d'une arête"""

    def __init__(self, n):
        """construit une matrice d'ordre n, représentant un graphe
        à n sommets sans arêtes"""

    def ajouter_arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie la matrice afin de créer un arc de s1 à s2"""

    def arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        renvoie un booléen précisant l'existence ou non d'un arc de s1 à s2"""

    def ajouter_arete(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie la matrice afin de créer une arete de s1 à s2"""

    def voisins(self, s):
        """prend en parametre un sommet s et
        renvoie la liste de ses voisins
        (il existe une arc de s à chaque voisin)"""

    def affiche(self):
        """affiche sur une ligne pour chaque sommet l'ensemble de ses voisins
        (dans un ordre indifférent)
        par ex :
        0 --> 1 3
        1 --> 2 3
        2 --> 3
        3 --> 1
        """
        # à compléter...
        pass
