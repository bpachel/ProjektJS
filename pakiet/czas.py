from datetime import datetime
from datetime import timedelta

"""Funkcje oraz klasy do obsługi czasu
"""

def changeTime(H, M):
    """Funkcja służy do zmiany godziny
    """
    now = datetime.now()
    delta = timedelta(
        minutes = M,
        hours=H
    )
    return now+delta


def getTime(now):
    '''Funkcja getTime zmienia czas na bardziej czytelniejszą wersje.
    '''
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    return dt_string

def getTimeArray(now):
    '''Funkcja getTimeArray zmienia podany czas
    na tablice liczbową w celu ułatwienia obliczeń.
    '''
    dt_string = now.strftime("%w:%d:%m:%Y:%H:%M")
    results = list(map(int, dt_string.split(":")))
    #funkcja zwraca tablce w formacie [numer dnia(0), dzień(1), miesiąc(2), rok(3), godzina(4), minuta(5)]
    return results

def timeAfterPayment(time, H, M):
    '''Funkcja timeAfterPayment oblicza,
    do jakiej daty i godziny możemy mieć zaparkowane auto.
    '''
    timeArray = getTimeArray(time)

    #gdy aktualny czas miesci się w czasie pracy parkomatu
    if (timeArray[4] >= 8 and timeArray[4] < 20):
        if(timeArray[5]+M>=60):
            H+=1
            M=(timeArray[5]+M)-60-timeArray[5]
        #dostosowanie ilości dni
        D=H//12
        H-=D*12
        if(timeArray[4]+H>=20):
            #zwiększenie o 1 liczbę dni gdyż czas po zapłacie przekracza godzinę 20
            D+=1

            #dostosowanie ilości godzin
            H=-1*(timeArray[4]-((timeArray[4]+H-20)+8))

            #kwestia wolnych dni tygodnia
            if((timeArray[0]+D)%7==0):
                D+=1
            if((timeArray[0]+D)%7==6):
                D+=2
    #gdy aktualny czas NIE miesci się w czasie pracy parkomatu
    elif (timeArray[4] >= 20):
        M=M-timeArray[5]
        #dostosowanie ilości dni
        D=H//12
        H-=D*12
        D+=1

        #dostosowanie ilości godzin
        tmp = timeArray[4]-8
        H=-1*(tmp-H)
        if((timeArray[0]+D)%7==0):
            D+=1
        if((timeArray[0]+D)%7==6):
            D+=2
    elif(timeArray[4] < 8):
        M=M-timeArray[5]
        #dostosowanie ilości dni
        D=H//12
        H-=D*12
        
        #dostosowanie ilości godzin
        tmp = 8-timeArray[4]
        H+=tmp
        if((timeArray[0]+D)%7==0):
            D+=1
        if((timeArray[0]+D)%7==6):
            D+=2

    #zmienna która jest dodawana do aktualnego czasu
    delta = timedelta(
        days=D,
        minutes = M,
        hours=H
    )
    time = time + delta
    return getTime(time)

