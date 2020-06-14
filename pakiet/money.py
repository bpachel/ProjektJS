import pakiet.error as err
class Pieniadz():
    """klasa Pieniadz
    """
    def __init__(self, wartosc):
        self._wartPien = wartosc
        try:
            for w in [(10**x)*y for x in range(4) for y in [0.01, 0.02, 0.05]]:
                if self._wartPien == w:
                    break
            else:
                raise err.ZlaWartoscNominalu(self._wartPien)
                self._wart=0.00
        except err.ZlaWartoscNominalu as e:
            print(e)
            raise
    def getWart(self):
        return round(self._wartPien, 2)

class Moneta(Pieniadz):
    """klasa Moneta dziedziczącza po klasie Pieniadz
    """
    def __init__(self, wartosc):
        self._wartMon = wartosc
        try:
            for w in [(10**x)*y for x in range(3) for y in [0.01, 0.02, 0.05]]:
                if self._wartMon == w:
                    break
            else:
                raise err.ZlaWartoscNominalu(self._wartMon)
                self._wart=0.00
        except err.ZlaWartoscNominalu as e:
            print(e)
            raise

class Banknot(Pieniadz):
    """klasa Banknot dziedziczącza po klasie Pieniadz
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