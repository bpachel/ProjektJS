from tkinter import *
from pakiet.money import Banknot
from pakiet.money import Moneta
from pakiet.automat import Parkometr
import pakiet.czas as czas
from datetime import datetime

pieniadz=0.01
def up(event):
    global pieniadz
    lista = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
    for x in range(len(lista)-1, -1, -1):
        if pieniadz==lista[len(lista)-1]:
            break
        elif pieniadz==lista[x]:
            pieniadz=lista[x+1]
    print(pieniadz)
            
def down(event):
    global pieniadz
    lista = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
    for x in range(len(lista)):
        if pieniadz==lista[0]:
            break
        elif pieniadz==lista[x]:
            pieniadz=lista[x-1]
    print(pieniadz)
            
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
window = Tk()
window.title("Parkometr 2020")
window.configure(background="black")
#Label(window, text="Wrzuć pieniądze:",bg="black", fg="white", font="none 12 bold").grid(row=0,column=1,sticky=W)

#tekst=Entry(window, width=20, bg="white")
#tekst.grid(row=2, column=1, sticky=W)

opis = Label(window, text="Wrzuć pieniądze:",bg="black", fg="white", font="none 12 bold")
wartosc = Label(window, textvariable=pieniadz,bg="black", fg="white", font="none 12 bold")
buttonUp = Button(window, text="up")
buttonDown = Button(window, text="down")

buttonUp.bind("<Button-1>", up)
buttonDown.bind("<Button-1>", down)

opis.pack()
buttonUp.pack()
wartosc.pack()
buttonDown.pack()
"""
frameAccept = Frame(window)
frameCancel = Frame(window)
frameAccept.pack(side=BOTTOM)
frameCancel.pack(side=BOTTOM)



buttonCancel = Button(frameCancel, text="ANULUJ", fg="red")
buttonAccept = Button(frameAccept, text="POTWIERDŹ", fg="green")

buttonCancel.pack()
buttonAccept.pack()
"""
window.mainloop()