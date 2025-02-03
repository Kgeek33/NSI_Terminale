class Ville:
    """ classe définissant une ville de France.
    Chaque ville a 4 attributs :
    - npm
    - numero de departement
    - population (hab)
    - superficie (km^2)
    - rang au niveau national (place)"""

    def __init__(self, liste: list[str]):
        self.nom = liste[0]
        self.departement = int(liste[1])
        self.population = int(liste[2])
        self.superficie = float(liste[3])
        self.rang = int(liste[4])


ligne_liste = ["Nice", "06", "343123", "71.9", "5"]
ville = Ville(ligne_liste)
