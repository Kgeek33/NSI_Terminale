#exo 1
def recherche_motif(motif, texte):
    assert motif!=''
    res=[]
    i_motif=0
    i_texte=0
    dans_le_motif=False
    while i_texte < len(texte) :
#        print(dans_le_motif,i_texte,i_motif,texte[i_texte],motif[i_motif])
        if texte[i_texte]==motif[i_motif] :
            dans_le_motif=True
            i_motif+=1
            i_texte+=1
        else :
            if not dans_le_motif :
                 i_texte+=1
            dans_le_motif=False
            i_motif=0
            
        if  i_motif==len(motif) :
            res.append(i_texte-len(motif))
            i_motif=0
            dans_le_motif=False
        print(motif[i_motif:], texte[i_texte:],res)
    return res       
        

assert recherche_motif("ab", "")==[]
assert recherche_motif("ab", "cdcdcdcd")==[]
assert recherche_motif("ab", "abracadabra")==[0, 7]
assert recherche_motif("ab", "abracadabraab")==[0, 7, 11]
#exo 2
def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)
            
            
def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc

assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0)==[0, 1, 2, 3]
assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4)==[4, 5]