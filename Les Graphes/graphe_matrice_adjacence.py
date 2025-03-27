def num(car):
    "renvoie le numéro du caractère car"
    car_maj=car.upper()
    return (ord(car_maj)-ord('A'))

def carac(n):
    "renvoie le caractère majuscule de rang n"
    return chr(ord('A')+n)

class Graphe:
    """un graphe représenté par une matrice d'adjacence,
       où les sommets sont les entiers 0,1,...,n-1
       On ne traite pas les graphes pondérés ici :
       la matrice est une matrice de booléens qui désignent l'existence ou non d'une arête"""

    def __init__(self, n):
        """construit une matrice d'ordre n, représentant un graphe à n sommets sans arêtes"""
        self.n = n
        self.adj = [[False] * n for _ in range(n)]

    def ajouter_arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        modifie la matrice afin de créer un arc de s1 à s2"""
        self.adj[s1][s2] = True

    def ajouter_arete(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        crée un arc dans les deux sens entre s1 et s2"""
        self.ajouter_arc(s1, s2)
        self.ajouter_arc(s2, s1)

    def arc(self, s1, s2):
        """prend en parametres les sommets s1 et s2 et
        renvoie un booléen précisant l'existence ou non d'un arc de s1 à s2"""
        return self.adj[s1][s2]

    def voisins(self, s):
        """prend en parametre un sommet s et
        renvoie la liste de ses voisins, cad des sommets i tels que il existe un arc de s à i """
        v = []
        for i in range(self.n):
            if self.adj[s][i]:
                v.append(i)
        return v


    def affiche(self):
        """affiche sur une ligne pour chaque sommet l'ensemble de ses voisins (dans un ordre indifférent)
        par ex :
        0 --> 1 3
        1 --> 2 3
        2 --> 3
        3 --> 1
        """
        for s in range(self.n):
            print(carac(s),"-->",end=" ")
            for t in self.voisins(s): print(carac(t),end=" ")
            print()

    def degre(self,s):
        """renvoie le degré du sommet s"""
        return len(self.voisins(s))

    def nb_arcs(self,s):
        """renvoie le nombre total d'arcs"""
        nb_a = 0
        for s in range(self.n):
            nb_a+=self.degre(s)
        return(nb_a)
    
    def ordre(self):
        return self.n

def sommet_degre_max(g):
    """renvoie le sommet de degré max (sous forme d'entier)"""
    d_max=0
    s_max=None
    for s in range(g.ordre()):
        d=g.degre(s)
        if d_max<d:
            d_max=d
            s_max=s
    return s_max,d_max
            
def nb_arcs_db_sens(g) :
    """renvoie le nombre d’arcs à double sens du graphe g passé en paramètre."""
    n_arcs=0
    for s in range(g.ordre()):
        for t in range(g.ordre()):
            if g.arc(s,t) and g.arc(s,t): n_arcs+=1
    return n_arcs

    
    
def connexion(g,s):
    """renvoie la liste des voisins de s ou ceux dont s est un voisin dans le graphe g."""
    connectés=[]
    for t in range(g.ordre()):
            if g.arc(s,t) or g.arc(t,s) : connectés.append(t)
    return connectés

    


        
    


if __name__ == '__main__' :
    

    #creation de g1_test
    g1_test=Graphe(8)
    g1_test.ajouter_arete(num('a'),num('b'))
    g1_test.ajouter_arete(num('a'),num('c'))
    g1_test.ajouter_arete(num('c'),num('d'))
    g1_test.ajouter_arete(num('d'),num('b'))
    g1_test.ajouter_arete(num('b'),num('e'))
    g1_test.ajouter_arete(num('d'),num('e'))
    g1_test.ajouter_arete(num('e'),num('g'))
    g1_test.ajouter_arete(num('e'),num('f'))
    g1_test.ajouter_arete(num('f'),num('g'))
    g1_test.ajouter_arete(num('g'),num('h'))

    print("g1_test :")

    g1_test.affiche()
    s='d';print("degre de",s,"=",g1_test.degre(num(s)))
    s,d=sommet_degre_max(g1_test)
    print("sommet de degre max:",carac(s),"de degré",d)
    print("nb d'arcs à double sens (arêtes):",nb_arcs_db_sens(g1_test))
    print('connexions:')
    for s in range(g1_test.ordre()):
        print(carac(s),":",[carac(t) for t in connexion(g1_test,s)])
    
    #creation de g2_test
    g2_test=Graphe(7)
    g2_test.ajouter_arc(num('A'),num('C'))
    g2_test.ajouter_arc(num('C'),num('A'))
    g2_test.ajouter_arc(num('A'),num('D'))
    g2_test.ajouter_arc(num('B'),num('A'))
    g2_test.ajouter_arc(num('D'),num('G'))
    g2_test.ajouter_arc(num('G'),num('D'))
    g2_test.ajouter_arc(num('G'),num('B'))
    g2_test.ajouter_arc(num('B'),num('G'))
    g2_test.ajouter_arc(num('E'),num('B'))
    g2_test.ajouter_arc(num('B'),num('F'))
    g2_test.ajouter_arc(num('E'),num('F'))
    g2_test.ajouter_arc(num('F'),num('E'))
    print("g2_test :")
    g2_test.affiche()
    s='E';print("degre de",s,"=",g2_test.degre(num(s)))
    s,d=sommet_degre_max(g2_test)
    print("sommet de degre max:",carac(s),"de degré",d)
    print("nb d'arcs à double sens (arêtes):",nb_arcs_db_sens(g2_test))
    print('connexions:')
    for s in range(g2_test.ordre()):
        print(carac(s),":",[carac(t) for t in connexion(g2_test,s)])

#test de taille
    import sys
    def taille_memoire(g):
        """renvoie la taille occupée par la matrice d'adjacence"""
        sz=0
        for s in range(g.ordre()):
            sz+=sys.getsizeof(g.adj[s])
        return sz
    
    g=Graphe(1000)
    print("taille en mémoire:",taille_memoire((g)))
    # rajouter un booleen dans une liste exige 4 octets suppléementaires
    a=[True]*1
    print(sys.getsizeof(a))
    a=[True]*2
    print(sys.getsizeof(a))
    a=[True]*3
    print(sys.getsizeof(a))
 
