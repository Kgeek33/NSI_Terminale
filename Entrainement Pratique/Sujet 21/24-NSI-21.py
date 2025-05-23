def recherche_motif(motif: str, text: str) -> list:
    P = []
    if motif not in text:
        return P
    k = 0
    g = 0
    while k < len(text):
        if g == len(motif):
            P.append(k - g)
            g = 0
        if motif[g] is not text[k]:
            g = 0
        if motif[g] is text[k]:
            g += 1
        k += 1
    if g == len(motif):
        P.append(k - g)
    return P


assert recherche_motif("ab", "") == []
assert recherche_motif("ab", "cdcdcdcd") == []
assert recherche_motif("ab", "abracadabra") == [0, 7]
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11]


def parcours(adj, x, acc: list):
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


assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0) == [0, 1, 2, 3]
assert accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4) == [4, 5]
