

def recherche_dichotomique (t,v):
    pass



if __name__ == '__main__' :
    def nextFibo(um2,um1):
        return um1,um2+um1

    def seqFibo(n):
        umoins2=0;umoins1=1
        F=[umoins2,umoins1]
        for i in range(2,n):
            umoins2,umoins1=nextFibo(umoins2,umoins1)
            F.append(umoins1)
        return F

    T=seqFibo(16)
    print(T)
    print("55 est à la position",recherche_dichotomique(T,55))        # -> 10
    print("56 est à la position",recherche_dichotomique(T,56))        # -> None
    print("377 est à la position",recherche_dichotomique(T,377))      # -> 14
    print("610 est à la position",recherche_dichotomique(T,610))      # -> 14
    print("10000 est à la position",recherche_dichotomique(T,10000))  # -> None
    print(recherche_dichotomique([0, 1, 1, 2, 3, 5, 8, 13, 21] , 7))
    T=seqFibo(32)
    print(T)
    print("55 est à la position",recherche_dichotomique(T,55))
    print("196418 est à la position",recherche_dichotomique(T,196418)) # -> 27

