class Graphe:
    """un graphe comme un dictionnaire d'adjacence ou les clés sont
    les sommets et les valeurs sont les listes des voisins """

    def __init__(self):
        # crée un dictionnaire vide
        self.adj = {}

    def ajouter_sommet(self, s):
        """ajoute, s'il n'existe pas déjà, le sommet s,
        sans arcs en provenance ou vers les autres sommets"""
        # à compléter...
        pass

    def ajouter_arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie le dictionnaire afin de créer un arc de s1 à s2"""
        # à compléter...
        pass

    def arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        renvoie un booléen précisant l'existence ou non d'un arc de s1 à s2"""
        # à compléter...
        pass

    def sommets(self):
        """renvoie la liste des sommets"""
        # à compléter...
        pass

    def voisins(self, s):
        """prend en parametre un sommet s et
        renvoie la liste de ses voisins"""
        # à compléter...
        pass

    def affiche(self):
        """affiche sur une ligne pour chaque sommet l'ensemble de ses voisins
        (dans un ordre indifférent)
        par ex :
        A --> B D
        B --> C D
        C --> D
        D --> A
        """
        # à compléter...
        pass
