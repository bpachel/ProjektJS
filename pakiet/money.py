import pakiet.error as err

class Moneta:
    """klasa Moneta
    """
    def __init__(self, wartosc):
        self._wartMon = int(wartosc*100)
        try:
            for w in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
                if self._wartMon == w:
                    break
            else:
                raise err.ZlaWartoscNominalu(self._wartMon)
                self._wart=0.00
        except err.ZlaWartoscNominalu as e:
            print(e)
            raise
    def getWart(self):
        return round(self._wartMon/100, 2)

class Banknot:
    """klasa Banknot
    """
    def __init__(self, wartosc):
        self._wartBan = int(wartosc)
        try:
            for w in [10, 20, 50]:
                if self._wartBan == w:
                    break
            else:
                raise err.ZlaWartoscNominalu(self._wartBan)
                self._wart=0.00
        except err.ZlaWartoscNominalu as e:
            print(e)
            raise
    def getWart(self):
        return self._wartBan


'''        
def wrzuc(wart, liczba):
    pass
'''