def correspond(mot: str, mot_a_trous: str) -> bool:
    mot_a_trous = list(mot_a_trous)
    mot = list(mot)

    for i in range(len(mot_a_trous)):
        if mot_a_trous[i] == "*":
            mot_a_trous[i] = mot[i]

    mot_a_trous = str(mot_a_trous)
    mot = str(mot)

    return mot == mot_a_trous


assert correspond("INFORMATIQUE", "INFO*MA*IQUE") == True
assert correspond("AUTOMATIQUE", "INFO*MA*IQUE") == False
assert correspond("STOP", "S*") == False
assert correspond("AUTO", "*UT*") == True


def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1

    return nb_destinataires == len(plan)


assert est_cyclique({'A': 'E', 'F': 'A', 'C': 'D',
                    'E': 'B', 'B': 'F', 'D': 'C'}) == False
assert est_cyclique({'A': 'E', 'F': 'C', 'C': 'D',
                    'E': 'B', 'B': 'F', 'D': 'A'}) == True
assert est_cyclique({'A': 'B', 'F': 'C', 'C': 'D',
                    'E': 'A', 'B': 'F', 'D': 'E'}) == True
assert est_cyclique({'A': 'B', 'F': 'A', 'C': 'D',
                    'E': 'C', 'B': 'F', 'D': 'E'}) == False
