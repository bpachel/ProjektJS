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

"""Funkcje oraz klasy do obsługi automatu
Automat powinien być czyms w rodzaju skarbonki
o maksymalnej pojemności 200 z każdego nominału

Dodatkowo możliwość wrzucania monet pradopodobnie tutaj

"""