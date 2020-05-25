class Moneta:
    """klasa Moneta
    """
    def __init__(self, wartosc):
        self._wartMon = int(wartosc*100)
        for w in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
            if self._wartMon == w:
                break
        else:
            #dodac obsluge blędów
            pass
    def getWart(self):
        return round(self._wartMon/100, 2)

class Banknot:
    """klasa Banknot
    """
    def __init__(self, wartosc):
        self._wartMon = int(wartosc)
        for w in [10, 20, 50]:
            if self._wartMon == w:
                break
        else:
            #dodac obsluge blędów
            pass
    def getWart(self):
        return self._wartMon
moneta = Moneta(0.01)
banknot = Banknot(11)
print(moneta.getWart())
print(banknot.getWart())