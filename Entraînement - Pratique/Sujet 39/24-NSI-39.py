def recherche(elt, tab):
    indice = None
    for i in range(len(tab)):
        if tab[i] == elt:
            indice = i
    return indice

assert recherche(1, [2, 3, 4]) == None# renvoie None
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 0, 42, 7]) == 0
assert recherche(1, [1, 50, 1]) == 2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5


class AdresseIP:
    def __init__(self, adresse):
        self.adresse =... 

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = [ ... ] 
        return ... 

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = ... 
        if ... == 254: 
            return None
        octet_nouveau = ... + ... 
        return AdresseIP('192.168.0.' + ...) 

