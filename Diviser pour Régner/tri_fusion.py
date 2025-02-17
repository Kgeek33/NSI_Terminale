
def fusion_iter(L,R):
    """prend deux listes L et R triées et renvoie la fusion T triée des deux listes """
    i,j=0,0
    T=[]
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            T.append(L[i])
            i+=1
        else:
            T.append(R[j])
            j+=1
    #une des deux listes est entièrement traitée
    if i>=len(L) : T=T+R[j:]     # L est entièrement traitée, s'il restait des elts de R non traités, ils sont ajoutés à T
    if j>=len(R) : T=T+L[i:]     # R est entièrement traitée, s'il restait des elts de L non traités, ils sont ajoutés à T
    #print(T)
    return T


def fusion_rec(L,R, cpt=0):
    """prend deux listes L et R triées et renvoie la fusion T triée des deux listes """
    cpt+=1
    #print("cpt fusion rec=",cpt)
    if L == [] : return R
    if R == [] : return L
    #le min de la fusion est le min des deux min
    if L[0]<=R[0]: return [L[0]]+fusion_rec(L[1:],R,cpt)
    else : return [R[0]]+fusion_rec(L,R[1:],cpt)

def diviser(lst):
    """prend une liste lst et renvoie deux listes correspondant à la moitié droite et à la moitié gauche"""
    milieu = len(lst)//2
    return lst[:milieu],lst[milieu:]


def tri_fusion (lst):
    if len(lst)<2 : return lst
    left,right=diviser(lst)
    #print(left,right)
    return fusion_iter(tri_fusion(left),tri_fusion(right))

if __name__ == '__main__' :

    print("test de la fusion")
    liste1=[3,5,8,9]
    liste2=[1,2,6,10,14,45]
    print("fusion iter {} et {} : {}".format(liste1,liste2,fusion_iter(liste1,liste2)))
    print("fusion iter {} et {} : {}".format(liste2,liste1,fusion_iter(liste2,liste1)))
    assert fusion_iter(liste1,liste2)==fusion_rec(liste1,liste2)
    assert fusion_iter(liste2,liste1)==fusion_rec(liste2,liste1)


    vrac=[3,4,6,2,5,1,8,7]
    print("en vrac :",vrac)
    print("en ordre :" , tri_fusion (vrac))


    vrac=[30,4,26,28,15,12,80,71,54]
    print("en vrac :",vrac)
    print("en ordre :" , tri_fusion (vrac))


    #benchs

    from tri_insertion import *

##    from triSelectionMinimum import triSelection


    from random import randint
    import timeit, functools
    from time import perf_counter

    def unTableau(min,max,n) :
        """renvoie un tableau de n entiers entre min et max compris"""
        t=[]
        for i in range(n):
            t.append(randint(min,max))
        return t

#test de la récursivité
    def tri_fusion_rec (lst, cpt=0):
        cpt+=1
        #print("cpt tri fusion rec=",cpt)
        if len(lst)<2 : return lst
        left,right=diviser(lst)
        #print(left,right)
        return fusion_rec(tri_fusion_rec(left,cpt),tri_fusion_rec(right,cpt))

    A=0
    N=10000
    B=A+N*10

    V=unTableau(A,B,18)
    print("en vrac :",V)
    print("en ordre :" , tri_fusion (V))
    print("en vrac :",V)
    print("en ordre :" , tri_fusion_rec (V))

# tests de performance
    def temps_d_exécution(f,x):
##        print("{} avec timeit et x={}".format(f,x))
##        print(timeit.timeit(functools.partial(f, x),number=1))
        print("perf_counter de {} avec n={}".format(f,len(x)))
        t1=perf_counter()
        r=f(x)
        t2=perf_counter()
        print("temps écoulé=",t2-t1)
    A=0
    B=100000

    for k in range (1,8):
        V=unTableau(A,B,100*2**k)
        temps_d_exécution(tri_insertion,V)
    for k in range (1,8):
        V=unTableau(A,B,100*2**k)
        temps_d_exécution(tri_fusion,V)
