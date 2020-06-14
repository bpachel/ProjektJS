from tkinter import *
from pakiet.money import Banknot
from pakiet.money import Moneta
from pakiet.automat import Parkomat
import pakiet.error as err
import pakiet.czas as czas
from datetime import datetime


parkomat = Parkomat()
window = Tk()

var = DoubleVar()
var.set(0.01)
dane = StringVar()
now = datetime.now()

opis1 = Label(window, text="Numer rejestracyjny:",bg="#A6CEE9", fg="black", font="none 12 bold", width=30)
opis2 = Label(window, text="Nominał:",bg="#A6CEE9", fg="black", font="none 12 bold", width=30)
opis3 = Label(window, text="Ilość:",bg="#A6CEE9", fg="black", font="none 12 bold", width=15)
godzina = Label(window, text="Minuta:",bg="#A6CEE9", fg="black", font="none 12 bold", width=15)
minuta = Label(window, text="Godzina:",bg="#A6CEE9", fg="black", font="none 12 bold", width=15)
wartosc = Label(window, textvariable=var,bg="#A6CEE9", fg="black", font="none 12 bold", width=15)
wynik = Label(window, textvariable=dane,bg="#A3C5DB", width=60, fg="black", font="none 12 bold")

ilosc = Entry(window, bg="white", width=15)
poleTablicy = Entry(window, bg="white", width=30)

buttonUpH = Button(window, text="+", command= lambda: globals().update(now=czas.changeTime(now, 1, 0)))
buttonUpM = Button(window, text="+", command= lambda: globals().update(now=czas.changeTime(now, 0, 1)))
buttonDownH = Button(window, text="-", command= lambda: globals().update(now=czas.changeTime(now, -1, 0)))
buttonDownM = Button(window, text="-", command= lambda: globals().update(now=czas.changeTime(now, 0, -1)))
buttonUp = Button(window, text="+")
buttonDown = Button(window, text="-")
buttonInsert = Button(window, text="wrzuc", width=15)
buttonAccept = Button(window, text="Zatwierdz", width=30)
buttonCancel = Button(window, text="Anuluj", width=30)

def up(event):
    pieniadz=var.get()
    lista = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
    for x in range(len(lista)-1, -1, -1):
        if pieniadz==lista[len(lista)-1]:
            break
        elif pieniadz==lista[x]:
            pieniadz=lista[x+1]
    var.set(pieniadz)
    window.update()
    print(pieniadz)
            
def down(event):
    pieniadz=var.get()
    lista = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
    for x in range(len(lista)):
        if pieniadz==lista[0]:
            break
        elif pieniadz==lista[x]:
            pieniadz=lista[x-1]
    var.set(pieniadz)
    window.update()
    print(pieniadz)



def wrzuc(event):
    global now
    try:
        if (ilosc.get()==""):
            raise err.BrakMonetExeption()
    except err.BrakMonetExeption as e:
        print(e)
        raise
    else:
        ileMonet = int(ilosc.get())
    pieniadz = var.get()
    #print(pieniadz, "x", ileMonet)
    dane.set("Aktualna godzina: " + czas.getTime(now) + "\n" + parkometr.wrzuc(pieniadz,now, ileMonet)
    #print(parkometr.getIleWrzucono())

def zatwierdz(event):
    global now
    tabRej = poleTablicy.get()
    dane.set(parkomat.zatwierdz(now,tabRej))
    window.update()

def anuluj(event):
    parkomat.anuluj()
    dane.set("Transakcja anulowana...")
    window.update()

def aktualizuj(event):
    dane.set("Aktualna godzina: " + czas.getTime(now) + "\n Cos tam cos tam")

def wyswietl():
    global now
    tekst = dane.get()
    txt = tekst.split("\n")
    dane.set("Aktualna godzina: " + czas.getTime(now) + txt[1])
    window.after(1000, wyswietl)


            
#WYKOMBINOWAĆ GDZIE DAĆ WYRAŻENIA LAMBDA
'''
przetestować w godzinach między 8 a 20, oraz miedzy 20 a 24
now = datetime.now()
print(czas.timeAfterPayment(now, 9, 12))
'''
"""
now = datetime.now()
#now = czas.changeTime(9, 10)
parkometr = Parkometr()
#wrzuc(self, nominal, ilosc)
parkometr.wrzuc(0.01, 150)
parkometr.wrzuc(0.02, 150)
parkometr.wrzuc(0.05, 30)
parkometr.wrzuc(20, 1)
parkometr.anuluj()
parkometr.wrzuc(0.01, 200)
#print(parkometr.getIleWrzucono())
print(parkometr.zatwierdz(now, "JAK678DS"))

#Muszą się zerować minuty!!!! 
"""

window.title("Bartlomiej Pachel 130561")
window.configure(background="#A6CEE9")
#Label(window, text="Wrzuć pieniądze:",bg="black", fg="white", font="none 12 bold").grid(row=0,column=1,sticky=W)

#tekst=Entry(window, width=20, bg="white")
#tekst.grid(row=2, column=1, sticky=W)


buttonUp.bind("<Button-1>", up)
buttonDown.bind("<Button-1>", down)
buttonInsert.bind("<Button-1>", wrzuc)
buttonAccept.bind("<Button-1>", zatwierdz)
buttonCancel.bind("<Button-1>", anuluj)
buttonUpH.bind("<Button-1>", aktualizuj)
buttonUpM.bind("<Button-1>", aktualizuj)
buttonDownH.bind("<Button-1>", aktualizuj)
buttonDownM.bind("<Button-1>", aktualizuj)

wynik.grid(row=0, column=0, columnspan=4, rowspan=2)
godzina.grid(row=2, column=0, rowspan=2)
buttonUpH.grid(row=2, column=1)
buttonUpM.grid(row=2, column=3)
buttonDownH.grid(row=3, column=1)
buttonDownM.grid(row=3, column=3)
minuta.grid(row=2, column=2, rowspan=2)
opis1.grid(row=4, column=0, columnspan=2)
poleTablicy.grid(row=4, column=2, columnspan=2)
buttonUp.grid(row=5, column=2)
opis2.grid(row=6, column=0, columnspan=2)
wartosc.grid(row=6, column=2)
buttonDown.grid(row=7, column=2)
opis3.grid(row=8, column=0, columnspan=2)
ilosc.grid(row=8, column=2)
buttonInsert.grid(row=8, column=3)
buttonCancel.grid(row=9, column=0, columnspan=2)
buttonAccept.grid(row=9, column=2, columnspan=2)

wyswietl()
window.mainloop()