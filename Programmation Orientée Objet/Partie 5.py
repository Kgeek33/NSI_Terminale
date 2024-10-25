from math import sqrt


def exercice4():
    class Chrono:
        def __init__(self, heures, minutes, secondes) -> None:
            self.heu = heures
            self.min = minutes
            self.sec = secondes
            while self.sec >= 60:
                self.sec -= 60
                self.min += 1
            while self.min >= 60:
                self.min -= 60
                self.heu += 1

        def __str__(self) -> str:
            return ("{}h {}m {}s".format(self.heu, self.min, self.sec))

        def clone(self):
            test = Chrono(self.heu, self.min, self.sec)
            return test

        def avance(self, t):
            self.sec += t
            while self.sec >= 60:
                self.sec -= 60
                self.min += 1

            while self.min >= 60:
                self.min -= 60
                self.heu += 1

            return self

        def egale(self, deuxieme):
            if self.heu == deuxieme.heu and self.min == deuxieme.min and self.sec == deuxieme.sec:
                return True
            return False

    class Chrono2:
        def __init__(self, secondes) -> None:
            sec = secondes
            min = 0
            heu = 0
            while sec >= 60:
                sec -= 60
                min += 1
            while min >= 60:
                heu += 1
                min -= 60
            self.time = [heu, min, sec]

        def __str__(self) -> str:
            return ("{}h {}m {}s".format(self.time[0], self.time[1], self.time[2]))

        def clone(self):
            sec = self.time[2]
            min = self.time[1]
            heu = self.time[0]
            while heu > 0:
                heu -= 1
                min += 60
            while min > 0:
                min -= 1
                sec += 60
            test = Chrono2(sec)
            return test

        def avance(self, t):
            self.time[2] += t
            while self.time[2] >= 60:
                self.time[2] -= 60
                self.time[1] += 1

            while self.time[1] >= 60:
                self.time[1] -= 60
                self.time[0] += 1

            return self

        def egale(self, deuxieme):
            if self.time[0] == deuxieme.time[0] and self.time[1] == deuxieme.time[1] and self.time[2] == deuxieme.time[2]:
                return True
            return False

    # t = Chrono(21, 34, 55)
    t = Chrono2(3600)
    print(str(t))
    u = t.clone()
    print(str(u))
    print(t.egale(u))
    t.avance(5)
    print(str(t))
    print(t.egale(u))


def exercice5():
    class Point:
        def __init__(self, nom, x, y) -> None:
            self.nom = nom
            self.x = x
            self.y = y

        def __str__(self) -> str:
            return ("{}({};{})".format(self.nom, self.x, self.y))

        def __eq__(self, p: object) -> bool:
            return p.x == self.x and p.y == self.y

        def distance_origine(self):
            x2 = (self.x)**2
            y2 = (self.y)**2
            total = sqrt(x2 + y2)
            return total

        def deplace(self, dx, dy):
            xd = self.x + dx
            yd = self.y + dy
            return Point(("{}'", xd, yd).__format__(self.nom))

        def distance(self, p):
            if (self == p):
                return 0
            else:
                x2 = (p.x - self.x)**2
                y2 = (p.y - self.y)**2
                total = sqrt(x2 + y2)
                return total

        def symetrique_O(self):
            return Point(("{}''").__format__(self.nom), -self.x, -self.y)

        def symetrique(self, p):
            pass

        def rotation_O(self, teta):
            pass


def exercice6():
    class Fraction:
        def __init__(self, num, denom) -> None: # `-> None` signifie le typage, tu peux skip
            # La condition d'abord avant de créer l'erreur
            if denom <= 0:
                raise ValueError()

            self.num = num
            self.denom = denom

        def __str__(self) -> str: # `-> str` signifie le typage, tu peux skip
            # J'ai généralisé, mais tu peux laisser ta condition
            return ("{}/{}").format(self.num, self.denom)

        def __eq__(self, f2: object) -> bool: # `f2: object` + `-> bool` signifient le typage, tu peux skip
            if self.num / self.denom == f2.num / f2.denom:
                return True

            return False

        def __lt__(self, f2: object) -> bool: # `f2: object` + `-> bool` signifient le typage, tu peux skip
            return (self.num * f2.denom - self.denom * f2.num < 0)
        
        def __add__(self, f2: object) -> None: # `f2: object` + `-> None` signifient le typage, tu peux skip
            self.num = self.num * f2.denom + f2.num * self.denom
            self.denom *= f2.denom # `*=` plutôt que `= self.denom *`
        
        def __mul__(self, f2: object) -> None: # `f2: object` + `-> None` signifient le typage, tu peux skip
            return Fraction(self.num * f2.num, self.denom * f2.denom)
        
        def irreductible(self) -> None: # `-> None` signifie le typage, tu peux skip
            a = self.num
            b = self.denom
            while self.denom > 0:
                r = self.num % self.denom
                self.num = self.denom
                self.denom = r
            self.denom = b // self.num
            self.num = a // self.num
        
        def inverse(self) -> None:
            return Fraction(self.denom, self.num)
    
    f = Fraction(12, 2)
    print(f.inverse())
    t = Fraction(15, 13)
    print(str(f))
    print(str(t))
    f.__add__(t)
    print(str(f))
    print(f == t) # à la place de `__eq__(t)`, faire `== t` exécute automatiquement `__eq__`
    print(f.__lt__(t))
    f.__mul__(t)
    print(str(f))
    f.irreductible()
    print(str(f))


# exercice4()
# exercice5()
exercice6()
