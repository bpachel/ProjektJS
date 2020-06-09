from pakiet.czas import timeAfterPayment
from pakiet.money import Banknot
from pakiet.money import Moneta

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

class parkometr():
    self._aktualnaWartosc = 0.0
    self._pojemnosc = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #przechowuje monety do zaplaty
    self._tmp = []

    #przechowuje monety którymi zostało opłacone parkowanie
    self._schowek = []

    def wrzuc(self, nominal, ilosc):
        if(nominal>5.0):
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
                            print("Dodano", x, "monet. Limit monet o nominale", round(nominal, 2), "wyczerpany, aby kontynuować wrzuć inny nominał.")
                            break
            

    
    def zatwierdz(self, txt):
        for x in self._tmp:
            if(x.getWart()>5.0):
                self._schowek.append(x)
            else:
                for num, wart in enumerate([0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0], 0):
                    if x.getWart() == wart:
                        self._schowek.append(x)
                        self._pojemnosc[num]+=1
        
        czasParkowania = timeAfterPayment(parkingTime(self._aktualnaWartosc))
        print(czasParkowania)
        self._tmp.clear()
        self._aktualnaWartosc = 0

    def anuluj(self):
        self._tmp.clear()
        self._aktualnaWartosc = 0

"""Funkcje oraz klasy do obsługi automatu
Automat powinien być czyms w rodzaju skarbonki
o maksymalnej pojemności 200 z każdego nominału

Dodatkowo możliwość wrzucania monet pradopodobnie tutaj

"""