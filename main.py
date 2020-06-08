from pakiet.money import Banknot
from pakiet.money import Moneta
import pakiet.czas as czas
from datetime import datetime

'''
przetestować w godzinach między 8 a 20, oraz miedzy 20 a 24
'''
now = datetime.now()
print(czas.timeAfterPayment(now, 9, 12))