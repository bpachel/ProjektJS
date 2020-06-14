from pakiet.czas import timeAfterPayment
from pakiet.money import Banknot
from pakiet.money import Moneta
import pakiet.error as err

def parkingTime(wart):
    """Funkcja obliczająca czas zaparkowania
    """
    if(wart<2.0):
        H=0
        M=int(60*(wart/2.0))
        return H, M
    elif(wart<6.0):
        wart-=2.0
        H=1
        M=int(60*(wart/4.0))
        return H, M
    else:
        wart-=6.0
        H=2
        H+=int(wart//5)
        M=int(60*((wart%5)/5.0))
        return H, M



#print(parkingTime(56))

class Parkomat():
    """Klasa służąca do osługi takich funkcji jak wrzuć, zatwierdz oraz anuluj.
    """
    def __init__(self):
        self._aktualnaWartosc = 0.0
        #do tej listy można uśyć list comprehension
        self._pojemnosc = [0 for x in range(9)]

        #przechowuje monety do zaplaty
        self._tmp = []

        #przechowuje monety którymi zostało opłacone parkowanie
        self._schowek = []

    def wrzuc(self, time, nominal, ilosc):
        """Funkcja ta pozwala na wrzucenie określonej ilości monet,
        o zadanym nominale.
        """
        if(nominal>5.0):
            for x in range(ilosc):
                self._tmp.append(Banknot(nominal))
                self._aktualnaWartosc+=nominal
        else:
            #do tej listy można uśyć list comprehension
            for num, wart in enumerate([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0], 0):
                if wart == round(nominal, 2):
                    if (ilosc + self._pojemnosc[num])<=200:
                        for x in range(ilosc):
                            self._pojemnosc[num]+=1
                            self._tmp.append(Moneta(nominal))
                            self._aktualnaWartosc+=round(nominal, 2)
                    else:
                        return("Wrzucono za dużo monet!!")
        H,M = parkingTime(round(self._aktualnaWartosc,2))
        czasParkowania = timeAfterPayment(time, H, M)
        return str("Parking do " + czasParkowania)
            

    def getIleWrzucono(self):
        """Funkcja zwraca wartość monet wrzuconych
        zaokrągloną do dwóch miejsc po przecinku
        """
        return round(self._aktualnaWartosc,2)

    def zatwierdz(self, time, numRejestr):
        """Funkcja zatwierdza i przekazuje monety do listy 'schowek'. #dodac sprawdzenie tablicy
        """
        try:
            if self._aktualnaWartosc == 0.0:
                raise err.BrakMonetExeption()
            elif(not (numRejestr.isalnum()) or not len(numRejestr)>0):
                raise err.ZlyNumerRejestracyjnyException()
        except err.BrakMonetExeption as e:
            print(e)
            return("Brak wrzuconych monet")
            raise
        except err.ZlyNumerRejestracyjnyException as e:
            print(e)
            return("Numer rejestracyjny nieprawidłowy!!")
            raise
        
        numRejestr = numRejestr.upper()
        for x in self._tmp:
            self._schowek.append(x)
        H,M = parkingTime(round(self._aktualnaWartosc,2))
        czasParkowania = timeAfterPayment(time, H, M)
        self._tmp.clear()
        self._aktualnaWartosc = 0
        return str("Zapłacone do " + czasParkowania + " dla numeru " + numRejestr)

    def anuluj(self):
        """Funkcja czyści zmienne
        """
        self._pojemnosc = [0 for x in range(9)]
        self._tmp.clear()
        self._aktualnaWartosc = 0
