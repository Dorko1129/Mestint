class Hanoi:
    def __init__(self,ke,c):
        self.kezdo=ke
        self.cel=c

    def celteszt (self,a):
        return a == self.cel

    def rakovetkezo (self, a):
        gyerekek=[]
        for honnan in range(3):
            for hova in range(3):
                tmp=True
                
                if honnan != hova:
                    if len(a[honnan]) > 0:
                        if len(a[hova]) != 0 and a[honnan][0] >= a[hova][0]:
                            tmp=False
                    else:
                        tmp=False
                else:
                    tmp=False

                if tmp == True:
                    uj_allapot=[list(rud) for rud in a]
                    korong = uj_allapot[honnan].pop(0)
                    uj_allapot[hova].insert(0, korong)
                    gyerekek.append(tuple(tuple(rud) for rud in uj_allapot))

        return gyerekek

if __name__ == '__main__':
    feladat= Hanoi(((1,2,3),(),()),((),(),(1,2,3)))
