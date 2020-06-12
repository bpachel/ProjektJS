from tkinter import *
from pakiet.money import Banknot
from pakiet.money import Moneta
from pakiet.automat import Parkometr
import pakiet.czas as czas
from datetime import datetime
parkometr = Parkometr()

window = Tk()
var = DoubleVar()
var.set(0.01)
dane = StringVar()
opis = Label(window, text="Wrzuć pieniądze:",bg="black", fg="white", font="none 12 bold")
wartosc = Label(window, textvariable=var,bg="black", fg="white", font="none 12 bold")
wynik = Label(window, textvariable=dane,bg="black", fg="white", font="none 12 bold")

ilosc = Entry(window, width=5, bg="white")
poleTablicy = Entry(window, width=5, bg="white")

buttonUp = Button(window, text="up")
buttonDown = Button(window, text="down")
buttonInsert = Button(window, text="wrzuc")
buttonAccept = Button(window, text="accept")
buttonCancel = Button(window, text="cancel")

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
    ileMonet = int(ilosc.get())
    pieniadz = var.get()
    print(pieniadz, "x", ileMonet)
    parkometr.wrzuc(pieniadz, ileMonet)
    print(parkometr.getIleWrzucono())

def zatwierdz(event):
    tabRej = poleTablicy.get()
    now = datetime.now()
    dane.set(parkometr.zatwierdz(now,tabRej))
    window.update()

def anuluj(event):
    parkometr.anuluj()
    dane.set("")
    window.update()



            
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

window.title("Parkometr 2020")
window.configure(background="black")
#Label(window, text="Wrzuć pieniądze:",bg="black", fg="white", font="none 12 bold").grid(row=0,column=1,sticky=W)

#tekst=Entry(window, width=20, bg="white")
#tekst.grid(row=2, column=1, sticky=W)


buttonUp.bind("<Button-1>", up)
buttonDown.bind("<Button-1>", down)
buttonInsert.bind("<Button-1>", wrzuc)
buttonAccept.bind("<Button-1>", zatwierdz)
buttonCancel.bind("<Button-1>", anuluj)

opis.grid(row=0, column=0, sticky=W, columnspan=2)
wartosc.grid(row=2, column=0, sticky=N)
ilosc.grid(row=2, column=1, sticky=N)
buttonUp.grid(row=1, column=0, sticky=N)
buttonDown.grid(row=3, column=0, sticky=N)
buttonInsert.grid(row=4, column=0, sticky=N, columnspan=2)
poleTablicy.grid(row=5, column=0, sticky=N, columnspan=2)
buttonCancel.grid(row=6, column=0, sticky=N)
buttonAccept.grid(row=6, column=1, sticky=N)
wynik.grid(row=7, column=0, sticky=N, columnspan=2)

window.mainloop()