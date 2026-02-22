class KancsoFeladat:
    def __init__(self, ke, c):
        self.kezdo = ke
        self.cel = c
        self.max1 = 3
        self.max2 = 5
        self.max3 = 8

    def celteszt(self, a):  # a = (a1, a2, a3) allapot
        return a[0] == self.cel or a[1] == self.cel or a[2] == self.cel

    def rakovetkezo(self, a):
        gyerekek = []
        # Egy tuple-be rakjuk a maximumokat, hogy index alapján (0, 1, 2) elérjük őket
        max_ertekek = (self.max1, self.max2, self.max3)

        # Két ciklussal végigmegyünk a lehetséges "honnan -> hova" párosításokon
        for forras in range(3):
            for cel_kancso in range(3):

                # Ugyanabba a kancsóba nem tudunk tölteni, ezt átugorjuk
                if forras == cel_kancso:
                    continue

                # Csak akkor töltünk, ha a forrásban VAN víz, a célban meg VAN HELY
                if a[forras] > 0 and a[cel_kancso] < max_ertekek[cel_kancso]:
                    # Kiszámoljuk a tölthető mennyiséget
                    T = min(a[forras], max_ertekek[cel_kancso] - a[cel_kancso])

                    # Ideiglenes lista
                    uj_allapot = list(a)
                    uj_allapot[forras] -= T
                    uj_allapot[cel_kancso] += T

                    # töltés
                    lepes_neve = f"tölt {forras + 1}->{cel_kancso + 1}"
                    gyerekek.append((lepes_neve, tuple(uj_allapot)))

        return gyerekek


if __name__ == '__main__':
    feladat = KancsoFeladat((0, 0, 8), 4)

    print("Az elérhető lépések:")
    print(feladat.rakovetkezo((0, 0, 8)))