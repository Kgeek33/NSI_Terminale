class Graphe:
    """un graphe comme un dictionnaire d'adjacence ou les clés sont
    les sommets et les valeurs sont les listes des voisins """

    def __init__(self):
        # crée un dictionnaire vide
        self.adj: dict[str, list[str]] = {}

    def ajouter_sommet(self, s):
        """ajoute, s'il n'existe pas déjà, le sommet s,
        sans arcs en provenance ou vers les autres sommets"""
        if s not in self.adj:
            self.adj[s] = []

    def ajouter_arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie le dictionnaire afin de créer un arc de s1 à s2"""
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if s2 not in self.adj[s1]:
            self.adj[s1].append(s2)

    def arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        renvoie un booléen précisant l'existence ou non d'un arc de s1 à s2"""
        if s1 in self.adj and s2 in self.adj:
            if s2 in self.adj[s1]:
                return True
            return False
        return False

    def ajouter_arete(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie le dictionnaire afin de créer un arc de s1 à s2"""
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        if s2 not in self.adj[s1]:
            self.adj[s1].append(s2)
        if s1 not in self.adj[s2]:
            self.adj[s2].append(s1)

    def sommets(self):
        """renvoie la liste des sommets"""
        s = []
        for key in self.adj:
            s.append(key)
        return s

    def ordre(self):
        return len(self.adj)

    def degre(self, s):
        return len(self.adj[s])

    def nb_arcs(self):
        s = 0
        for key in self.adj:
            s += len(self.adj[key])
        return s

    def voisins(self, s):
        """prend en parametre un sommet s et
        renvoie la liste de ses voisins"""
        return self.adj[s]

    def affiche(self):
        """affiche sur une ligne pour chaque sommet l'ensemble de ses voisins
        (dans un ordre indifférent)
        par ex :
        A --> B D
        B --> C D
        C --> D
        D --> A
        """
        for key in self.adj:
            print(key, "-->", self.voisins(key))


if __name__ == "__main__":
    g1_test = Graphe()
    g1_test.ajouter_arete("A", "B")
    g1_test.ajouter_arete("A", "C")
    g1_test.ajouter_arete("B", "D")
    g1_test.ajouter_arete("B", "E")
    g1_test.ajouter_arete("C", "D")
    g1_test.ajouter_arete("D", "E")
    g1_test.ajouter_arete("E", "F")
    g1_test.ajouter_arete("E", "G")
    g1_test.ajouter_arete("F", "G")
    g1_test.ajouter_arete("G", "H")
    g1_test.affiche()
    print("-----")

    g2_test = Graphe()
    g2_test.ajouter_arc(0, 2)
    g2_test.ajouter_arc(2, 0)
    g2_test.ajouter_arc(1, 0)
    g2_test.ajouter_arc(1, 6)
    g2_test.ajouter_arc(1, 5)
    g2_test.ajouter_arc(0, 3)
    g2_test.ajouter_arc(3, 6)
    g2_test.ajouter_arc(6, 3)
    g2_test.ajouter_arc(6, 1)
    g2_test.ajouter_arc(4, 1)
    g2_test.ajouter_arc(4, 5)
    g2_test.ajouter_arc(5, 4)
    g2_test.affiche()
    print(g2_test.nb_arcs())
    print(g2_test.nb_arcs_db_sens())
    print(g2_test.degre(0))
    print(g2_test.sommet_degre_max())
    print("-----")

