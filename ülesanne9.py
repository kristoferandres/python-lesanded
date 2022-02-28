# ülesanne 9
# Kristofer Andres
# 17.02.2022

from datetime import datetime
from dateutil.relativedelta import *
kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]

#inglise kuupäev
kuup = datetime.datetime.today()
kuupaeveng = kuup.strftime('%d.%B.%Y')

#eesti kuupäev
kuupaev = kuup.strftime('%d.%m.%Y')
d, m, Y = kuupaev.split('.')
kuu= kuud[int(m)-1]
kuupaevest = (d +"."+ kuu +"."+ Y)


print(kuupaeveng)
print(kuupaevest)

isikukood = 50503230231
isikukood = str(isikukood)
sünniaasta = "20" + isikukood[1:3]
sünnikuu = isikukood[3:5]
sünnipäev = isikukood[5:7]
sünnikuupäev = sünnipäev+'.'+sünnikuu+'.'+sünniaasta
laps= relativedelta(sünnikuupäev,kuupaev)
print("vanus= "laps)
