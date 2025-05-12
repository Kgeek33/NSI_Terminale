class Graphe:
    """un graphe comme un dictionnaire d'adjacence ou
    les clés sont les sommets et les valeurs sont les listes des voisins """

    def __init__(self):
        # crée un dictionnaire vide
        self.adj = {}

    def ajouter_sommet(self, s):
        """ajoute, s'il n'existe pas déjà, le sommet s, sans arcs en provenance ou vers les autres sommets"""
        if s not in self.adj:
            self.adj[s] = []

    def ajouter_arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie le dictionnaire afin de créer un arc de s1 à s2"""

        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if not s2 in self.adj[s1]:
            self.adj[s1].append(s2)

    def ajouter_arete(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie le dictionnaire afin de créer un arc de s1 à s2"""

        self.ajouter_arc(s1, s2)
        self.ajouter_arc(s2, s1)

    def arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        renvoie un booléen précisant l'existence ou non d'un arc de s1 à s2"""
        if not s1 in self.sommets() or not s2 in self.sommets():
            return False
        return s2 in self.adj[s1]

    def sommets(self):
        """renvoie la liste des sommets"""
        return list(self.adj.keys())

    def ordre(self):
        return len(self.sommets())

    def voisins(self, s):
        """prend en parametre un sommet s et
        renvoie la liste de ses voisins"""
        return self.adj[s]

    def degre(self, s):
        """renvoie le degré du sommet s"""
        return len(self.adj[s])

    def nb_arcs(self):
        """renvoie le nombre total d'arcs"""
        nb_a = 0
        for s in self.sommets():
            nb_a += len(self.voisins(s))
        return nb_a

    def affiche(self):
        """affiche sur une ligne pour chaque sommet l'ensemble de ses voisins (dans un ordre indifférent)
        par ex :
        A --> B C
        B --> A C
        C --> B
        """
        for s in self.sommets():
            print(s, "-->", end=" ")
            for t in self.voisins(s):
                print(t, end=" ")
            print()


def sommet_degre_max(g):
    """renvoie le sommet de degré max"""
    d_max = 0
    s_max = None
    for s in g.sommets():
        d = g.degre(s)
        if d_max < d:
            d_max = d
            s_max = s
    return s_max, d_max


def nb_arcs_db_sens(g):
    """renvoie le nombre d’arcs à double sens du graphe g passé en paramètre. sans tenir compte des boucles"""
    n_arcs = 0
    for s in g.sommets():
        for t in g.sommets():
            if g.arc(s, t) and g.arc(t, s):
                n_arcs += 1
    # chaque arete a été comptée deux fois
    return n_arcs/2


def connexion(g, s):
    """renvoie la liste des voisins de s ou ceux dont s est un voisin dans le graphe g."""
    connectés = []
    for t in g.sommets():
        if g.arc(s, t) or g.arc(t, s):
            connectés.append(t)
    return connectés


if __name__ == '__main__':

    def num(car):
        "renvoie le numéro du caractère car"
        car_maj = car.upper()
        return (ord(car_maj)-ord('A'))

    # creation de g1_test
    g1_test = Graphe()
    g1_test.ajouter_arete('a', 'b')
    g1_test.ajouter_arete('a', 'c')
    g1_test.ajouter_arete('c', 'd')
    g1_test.ajouter_arete('d', 'b')
    g1_test.ajouter_arete('b', 'e')
    g1_test.ajouter_arete('d', 'e')
    g1_test.ajouter_arete('e', 'g')
    g1_test.ajouter_arete('e', 'f')
    g1_test.ajouter_arete('f', 'g')
    g1_test.ajouter_arete('g', 'h')

    print("g1_test :")

    g1_test.affiche()
    print("nb d'arcs (*2 pour une arête) :", g1_test.nb_arcs())
    s = 'd'
    print("degre de", s, "=", g1_test.degre(s))
    s, d = sommet_degre_max(g1_test)
    print("sommet de degre max:", s, "de degré", d)
    print("nb d'arcs à double sens (arêtes):", nb_arcs_db_sens(g1_test))
    print('connexions:')
    for s in g1_test.sommets():
        print(s, ":", [t for t in connexion(g1_test, s)])

    # creation de g2_test
    g2_test = Graphe()
    g2_test.ajouter_arc('A', 'C')
    g2_test.ajouter_arc('C', 'A')
    g2_test.ajouter_arc('A', 'D')
    g2_test.ajouter_arc('B', 'A')
    g2_test.ajouter_arc('D', 'G')
    g2_test.ajouter_arc('G', 'D')
    g2_test.ajouter_arc('G', 'B')
    g2_test.ajouter_arc('B', 'G')
    g2_test.ajouter_arc('E', 'B')
    g2_test.ajouter_arc('B', 'F')
    g2_test.ajouter_arc('E', 'F')
    g2_test.ajouter_arc('F', 'E')
    print("g2_test :")
    g2_test.affiche()
    print("nb d'arcs (*2 pour une arête) :", g2_test.nb_arcs())
    s = 'E'
    print("degre de", s, "=", g2_test.degre(s))
    s, d = sommet_degre_max(g2_test)
    print("sommet de degre max:", s, "de degré", d)
    print("nb d'arcs à double sens (arêtes):", nb_arcs_db_sens(g2_test))
    print('connexions:')
    for s in g2_test.sommets():
        print(s, ":", [t for t in connexion(g2_test, s)])
