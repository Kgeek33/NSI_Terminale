#exo 1
def recherche0(elt,tab):
    #parcours en arrière et sortie à la première occurrence
    for k in range(len(tab)-1,-1,-1):
        if tab[k]==elt:
            return k

def recherche(elt,tab):
    #parcours en avant et memorisation de l'indice, renvoi à la fin du parcours
    indice = None
    for k in range(len(tab)):
        if tab[k]==elt:
            indice=k
    return indice

assert recherche(1, [2, 3, 4]) ==None
assert recherche(1, [10, 12, 1, 56])==2
assert recherche(1, [1, 0, 42, 7])==0
assert recherche(1, [1, 50, 1])==2
assert recherche(1, [8, 1, 10, 1, 7, 1, 8])==5


#exo 2
class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse 

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = [ '192.168.0.0' , '192.168.0.255' ] 
        return self.adresse in reservees 

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets() 
        if octets[3] == 254: 
            return None
        octet_nouveau = octets[3] + 1 
        return AdresseIP('192.168.0.' + str(octet_nouveau)) 

#instanciation des adresses 
adresse1=AdresseIP('192.168.0.1')
adresse2=AdresseIP('192.168.0.2')
adresse3=AdresseIP('192.168.0.0')

#print(adresse1.adresse,adresse1.liste_octets())
assert adresse1.liste_octets()==[192, 168, 0, 1]
assert adresse1.est_reservee()==False
assert adresse3.est_reservee()==True
assert adresse2.adresse_suivante().adresse =='192.168.0.3'