euros = (2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)


def rendre_monnaie(pieces: tuple, s: int | float):
    q = 0
    P = list(pieces)
    P.sort(reverse=True)
    M = []
    a_rendre = s
    while q < len(P) and a_rendre > 0:
        if a_rendre - P[q] > 0:
            a_rendre = round(a_rendre - P[q])
            M.append(P[q])
        else:
            q += 1
    return M


if __name__ == '__main__':
    print(rendre_monnaie(euros, 5.33))
