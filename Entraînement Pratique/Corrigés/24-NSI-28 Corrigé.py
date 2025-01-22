#exo1
# version itérative
def fibonacci(n):
    """prend en paramètre un entier n supposé strictement positif et
    qui renvoie le terme d’indice n de la suite"""
    assert n>0
    if n <= 2:
        return 1
    fibPr = 1
    fib = 1
    for num in range(2, n):
        fibPr, fib = fib, fib + fibPr
    return fib

#recursivité double
def fibo_rec_db(n):
    assert n>0
    if (n <= 2):
        return 1
    else:
        return fibo_rec_db(n-1) + fibo_rec_db(n-2)
#recursivité simple
def fibo_rec_simple(n):
    assert n>0
    def fib_rec(a, b, n):
        """recursive simple"""
        if n == 1:
            return a
        else:
            return fib_rec(b,a+b,n-1)
    return fib_rec(1, 1, n)



assert fibonacci(1)==fibo_rec_db(1)==fibo_rec_simple(1)==1
assert fibonacci(2)==fibo_rec_db(2)==fibo_rec_simple(1)==1
assert fibonacci(25)==fibo_rec_db(25)==fibo_rec_simple(25)==75025

#exo2
def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = [] 

    for i in range(len(notes)): 
        if notes[i] == note_maxi: 
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i] 
            meilleurs_eleves = [eleves[i]] 

    return (note_maxi, meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
assert eleves_du_mois(eleves_nsi, notes_nsi)==(80, ['c', 'f', 'h'])
assert eleves_du_mois([],[])==(0, [])

