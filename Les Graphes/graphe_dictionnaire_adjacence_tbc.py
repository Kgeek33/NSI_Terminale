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
        if s not in self.adj:
            s = {}

    def ajouter_arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie le dictionnaire afin de créer un arc de s1 à s2"""
        # à compléter...
        if s1 

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


G = {"A": -2, "B": 3, "C": 5}
# G est un dictionnaire
print("affiche les clés", G.keys())  # affiche les clés
print("affiche les valeurs", G.values())  # affiche les valeurs
print("affiche les clés,valeurs dans une liste", list(G.items()))
print("affiche les clés dans une liste", list(G.keys()))
print("affiche les valeurs dans une liste", list(G.values()))
print(len(G))  # affiche le nombre de clés
print(G["e"])  # affiche la valeur de la clé "e"
# G.keys() et G.values() sont itérables
# # affiche les valeurs du dictionnaire
for el in G.values():
    print(el)
# affiche les clés et les valeurs des clés
for key in G.keys():
    print(key, G[key])
for key in G:
    print(key, G[key])
