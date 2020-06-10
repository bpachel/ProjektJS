from pakiet.money import Banknot
from pakiet.money import Moneta
from pakiet.automat import Parkometr
import pakiet.czas as czas
from datetime import datetime

'''
przetestować w godzinach między 8 a 20, oraz miedzy 20 a 24
now = datetime.now()
print(czas.timeAfterPayment(now, 9, 12))
'''

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