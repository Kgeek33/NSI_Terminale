import random


class Personnage:
    def __init__(self, nom, nbre_vies) -> None:
        self.vie = nbre_vies
        self.nom = nom

    def __str__(self) -> str:
        return ("{} a {} points de vie".format(self.nom, self.vie))

    def get_etat(self):
        return self.vie

    def blesser(self, max_blessures):
        nbPoint = random.randint(1, max_blessures)
        if random.choice([True, False]) == True:
            print("Bilbo a doublé les dégâts !!!!" if self.nom ==
                  "Gollum" else "Gollum a doublé les dégâts !!!!")
            nbPoint *= 2
        self.vie -= nbPoint

    def boire_potion(self, cmb_soins):
        self.vie += cmb_soins


def game():
    bilbo = Personnage("Bilbo", 15)
    gollum = Personnage("Gollum", 20)
    print(str(bilbo))
    print(str(gollum))
    while bilbo.get_etat() > 0 and gollum.get_etat() > 0:
        bilbo.blesser(5)
        gollum.blesser(5)
        print("combat : " + str(bilbo) + "\n" + str(gollum))
        bilbo.boire_potion(random.randint(0, 5))
        gollum.boire_potion(random.randint(0, 5))
    if bilbo.get_etat() <= 0 and gollum.get_etat() > 0:
        msg = "Gollum est vainqueur, il lui reste encore {} points alors que Bilbo est mort".format(
            gollum.get_etat())
    elif gollum.get_etat() <= 0 and bilbo.get_etat() > 0:
        msg = "Bilbo est vainqueur, il lui reste encore {} points alors que Gollum est mort".format(
            bilbo.get_etat())
    else:
        msg = "Les deux combattants sont morts en même temps"
    return msg


print(game())
