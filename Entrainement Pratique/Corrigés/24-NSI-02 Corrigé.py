#exo 1
def correspond(mot,mot_a_trous):
    lg=len(mot)
    if lg !=len(mot_a_trous):
        return False
    for k in range(lg):
        if not mot_a_trous[k] == '*' and not mot_a_trous[k]==mot[k]:
            return False
    return True


assert correspond('INFORMATIQUE', 'INFO*MA*IQUE')==True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE')==False
assert correspond('STOP', 'S*')==False
assert correspond('AUTO', '*UT*')==True

#exo 2
def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages.
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan['A'] 
    nb_destinataires = 1

    while destinataire != 'A':
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires + 1

    return nb_destinataires == len(plan) 

assert est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})==False
assert est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})==True
assert est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})==True
assert est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})==False
