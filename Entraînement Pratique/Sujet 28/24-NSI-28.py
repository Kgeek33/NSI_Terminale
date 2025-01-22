def fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1

    m: list = [1, 1]
    for i in range(n):
        nsomme: int = m[i] + m[i + 1]
        m.append(nsomme)
    return m[n - 1]


assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(25) == 75025


def eleves_du_mois(eleves: list, notes: list) -> tuple:
    note_maxi: int = 0
    meilleurs_eleves: list = []

    for i in range(len(eleves)):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi, meilleurs_eleves)


eleves_nsi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
assert eleves_du_mois(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
assert eleves_du_mois([], []) == (0, [])
