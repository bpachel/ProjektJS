from pakiet.czas import timeAfterPayment
from pakiet.money import Banknot
from pakiet.money import Moneta
import pakiet.error as err

def parkingTime(wart):
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

class Parkometr():
    def __init__(self):
        self._aktualnaWartosc = 0.0
        self._pojemnosc = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        #przechowuje monety do zaplaty
        self._tmp = []

        #przechowuje monety którymi zostało opłacone parkowanie
        self._schowek = []

    def wrzuc(self, nominal, ilosc):
        if(nominal>5.0):
            for x in range(ilosc):
                self._tmp.append(Banknot(nominal))
                self._aktualnaWartosc+=nominal
        else:
            for num, wart in enumerate([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0], 0):
                if wart == round(nominal, 2):
                    for x in range(ilosc):
                        if (x+self._pojemnosc[num])<=200:
                            self._tmp.append(Moneta(nominal))
                            self._aktualnaWartosc+=round(nominal, 2)
                        else:
                            print("Dodano", x-1, "monet. Limit monet o nominale", round(nominal, 2), "wyczerpany, aby kontynuować wrzuć inny nominał.")
                            break
            

    def getIleWrzucono(self):
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
            raise
        except err.ZlyNumerRejestracyjnyException as e:
            print(e)
            raise
        
        numRejestr = numRejestr.upper()
        for x in self._tmp:
            if(x.getWart()>5.0):
                self._schowek.append(x)
            else:
                for num, wart in enumerate([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0], 0):
                    if x.getWart() == wart:
                        self._schowek.append(x)
                        self._pojemnosc[num]+=1
        H,M = parkingTime(round(self._aktualnaWartosc,2))
        czasParkowania = timeAfterPayment(time, H, M)
        self._tmp.clear()
        self._aktualnaWartosc = 0
        return str(czasParkowania+"\nDla auta o numerze rejestracynym " + numRejestr + " na czas " + str(H) +" godzin i " + str(M) + " minut.")

    def anuluj(self):
        self._tmp.clear()
        self._aktualnaWartosc = 0

"""Funkcje oraz klasy do obsługi automatu
Automat powinien być czyms w rodzaju skarbonki
o maksymalnej pojemności 200 z każdego nominału

Dodatkowo możliwość wrzucania monet pradopodobnie tutaj

"""