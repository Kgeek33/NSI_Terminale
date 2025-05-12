def exercice1():
    def un_calcul1(a, b, c):
        return (a+(b*c))

    print("calcul #1 : ", un_calcul1(10, 20, 30))

    def un_calcul2(a, b, c=300):
        return (a+(b*c))

    print("calcul #2a : ", un_calcul2(10, 20, 30))
    print("calcul #2b : ", un_calcul2(10, 20))

    def un_calcul3(a=100, b=200, c=300):
        return (a+(b*c))

    print("calcul #3a : ", un_calcul3(b=20))
    print("calcul #3b : ", un_calcul3())
    print("calcul #3d : ",
          un_calcul3(c=10, a=20, b=30))
    print("calcul #3e : ", un_calcul3(c=20, b=30))

    def un_calcul4(*par):
        s = 0
        for a in par:
            s = s+a
        return s

    print("calcul #4a : ", un_calcul4(1, 2, 3))
    print("calcul #4b : ", un_calcul4(2, 3, 1))
    print("calcul #4d : ", un_calcul4(123))
    print("calcul #4e : ", un_calcul4(3, 2, 1, -1, -2))
    print("calcul #4e : ", un_calcul4(3, -2))
    print("calcul #4f : ", un_calcul4())


exercice1()
