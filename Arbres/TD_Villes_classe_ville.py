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
        self.departement = f"0{int(liste[1])}" if int(
            liste[1]) < 10 else int(liste[1])
        self.population = int(liste[2])
        self.superficie = float(liste[3])
        self.rang = int(liste[4])

    def __str__(self):
        return (
            f"{self.affiche_nom()} ({self.departement}),"
            f"qui compte {self.population} "
            f"habitants et couvre un territoire de {self.get_superficie()}km2"
            ", est la "
            f"{self.get_rang()}ème ville de France"
        )

    def get_rang(self):
        return self.rang

    def get_superficie(self):
        return self.superficie

    def affiche_nom(self):
        return self.nom


ligne_liste = ["Nice", "06", "343123", "71.9", "5"]
ville = Ville(ligne_liste)
print(ville)
