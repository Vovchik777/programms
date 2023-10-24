import time
import time as t
import datetime
from datetime import *
while True:
    den = datetime.today()
    god = den.year+1
    newyer = datetime(god,1,1)
    print('До Нового Года:',newyer-den,end = "")
    t.sleep(1)
    print('\r\r',end='')
    print(type(den))
# print(den.date())
# den2 = den.date
# print(timedelta())

#denyear = list(str(den.year))
#print(denyear)
#god =
# print(datetime.date())
# sledgod = list(data)[0]
# print(sledgod)