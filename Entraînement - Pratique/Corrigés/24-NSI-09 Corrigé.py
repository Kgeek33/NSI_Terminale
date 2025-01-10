#exo 1
def effectif_notes(notes_eval):
    """prend en paramètre le tableau notes_eval et
    renvoie un tableau de longueur 11 tel que
    la valeur d’indice i soit le nombre de notesvalant i dans le tableau notes_eval"""
    effectifs = [0]*11
    # pour chaque note entre 0 et 10
    for note in range(11):
        cpt=0
        # decompte du nombre d'occurrence dans l'evaluation
        for elt in notes_eval :
            if elt == note :
                cpt+=1
        
        effectifs[note]=cpt
    return effectifs

def notes_triees(effectifs) :
    """prend en paramètre le tableau des effectifs des notes et
    renvoie un tableau contenant les mêmes valeurs que notes_eval
    mais triées dans l’ordre croissant."""
    classement=[]
    for note in range(len(effectifs)) :
        nb_occurrences= effectifs[note]
        for k in range(nb_occurrences):
            classement.append(note)
    return classement
        
   
notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7,9, 9, 5, 0, 9, 6, 5, 4]
eff = effectif_notes(notes_eval)
assert eff ==[2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1]
assert notes_triees(eff)==[0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10]

#exo 2

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    # si c'est la dernière division
    if q == 0: 
        return str(r) 
    else:
        return dec_to_bin(q) + str(r) 

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin[-1] == '0': 
            return 0
        else:
            return 1 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit 



assert dec_to_bin(25)=='11001'
assert bin_to_dec('101010')==42
assert bin_to_dec('1010101')==85


for k in range (100) :
    print(k,"= 0b"+dec_to_bin(k))
    assert bin_to_dec(dec_to_bin(k))==k